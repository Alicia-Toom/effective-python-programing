#!/usr/bin/env python
"""
References:
- https://docs.docker.com/engine/api/v1.41/
- https://docker-py.readthedocs.io/en/4.4.4/index.html
"""
import argparse
import datetime
import syslog
import docker

today = datetime.datetime.combine(datetime.date.today(), datetime.time())


def prune(args):
    """
    Remove containers that exited earlier than our cut off date
    and all unused images, volumes and networks
    """

    if args.verbose:
        log(f"""Running prune with cut_off_date_days:
            {args.cut_off_date_days}, dry_run: {args.dry_run}""")

    cut_off_date = today - datetime.timedelta(days=args.cut_off_date_days)
    client = docker.DockerClient(base_url=args.
        docker_client_url, user_agent="Volvofinans Docker Prune Job")

    for container in client.containers.list(filters={"status": "exited"}):
        finished_at = datetime.datetime.strptime(
            container.attrs["State"]["FinishedAt"][:19], "%Y-%m-%dT%H:%M:%S")
        if finished_at < cut_off_date:
            if not args.dry_run:
                container.remove()

            log(f"Removed container {container.id} with name {container.name}")
        else:
            if args.verbose:
                log(f"Ignored container {container.id} with name {container.name}")
    log("Pruned exited containers")


    def prune_unused_images():
        """
        Remove unused images
        """
        if not args.dry_run:
            images_cache = {image.id: image.attrs["RepoTags"] for image in client.images.list(all=True)}
            result = client.images.prune(filters={"dangling": False})
            if "ImagesDeleted" in result and result["ImagesDeleted"] is not None:
                for entry in result["ImagesDeleted"]:
                    if "Deleted" in entry and entry["Deleted"] is not None:
                        image_id = entry["Deleted"] if image_id in images_cache else "Unknown"
                        image_tags = ",".join(images_cache[image_id]) if image_id in images_cache else "Unknown"
                        log(f"Removed image {image_id} with tags [{image_tags}]")
        log("Pruned unused images")


    def prune_unused_volumes():
        """Remove unused volumes"""
        if not args.dry_run:
            volumes_cache = {volume.id: volume.name for volume in client.volumes.list()}
            result = client.volumes.prune()
            if "VolumesDeleted" in result and result["VolumesDeleted"] is not None:
                for volume_id in result["VolumesDeleted"]:
                    log(f"Removed volume {volume_id} with name {volumes_cache[volume_id]}")
        log("Pruned unused volumes")


    def prune_unused_networks():
        """Remove unused networks"""
        if not args.dry_run:
            result = client.networks.prune()
            if "NetworksDeleted" in result and result["NetworksDeleted"] is not None:
                for network in result["NetworksDeleted"]:
                    log(f"Removed network {network}")
        log("Pruned unused networks")

def log(msg):
    """
    printing message out
    """
    syslog.syslog(msg)
    print(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Volvofinans Docker Prune Job")
    parser.add_argument("--cut-off-date-days", help="specify the number of days"+
        "that will be used to calculate the cut-off date", type=int, default=7)
    parser.add_argument("--docker-client-url", help="specify the docker client"+
        " connection url", default="unix://var/run/docker.sock")
    parser.add_argument("--dry-run", help="run prune job in dry run mode displaying"+
        " what will be removed without any action", action="store_true")
    parser.add_argument("--verbose", help="run prune job in verbose mode", action="store_true")

    prune(parser.parse_args())
