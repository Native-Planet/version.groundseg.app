#### Native Planet software version server

Serves a JSON blob with current version information for all software.

Gets updated by authenticated webhook called by Jenkins build jobs.

Stores data in sqlite db.

```json
{
"groundseg":
    {
        "latest": {
            "groundseg": {
                "major": 1,
                "minor": 0, 
                "patch": 8,
                "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_latest",
                "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_latest",
                "amd64_sha256": "c170b2b5111ea7b88db798b0740fa8d3e3eeaa02f6b42c4fdda73a52cae7b969",
                "arm64_sha256": "769200017da12766728cab8f17bc11bbc4cd5a9540cc919b364649aa74cc2cdd"
            },
            "webui": {
                "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
                "tag": "latest",
                "sha256": "3192699f1a69468b121d006eadde61026f2a149a6a4223602fb25464ae000a26"
            },
            "vere": {
                "repo": "registry.hub.docker.com/nativeplanet/urbit",
                "tag": "v1.20",
                "sha256": "16a1d2e80e4000555dd53a4e918ad72501f5bc827722fa113a348024f97d4a8f"
            },
            "minio": {
                "repo": "registry.hub.docker.com/minio/minio",
                "tag": "latest",
                "sha256": "a0a002cb113c3fc6b0a8d4a7a8ebaa8d151a734290db9f92a234b95573753aef"
            },
            "miniomc": {
                "repo": "registry.hub.docker.com/minio/mc",
                "tag": "latest",
                "sha256": "ad34abeba912fa92f3cc4b462d53370a2eab07c59ca7c9c851656972e3d42f84"
            },
            "wireguard": {
                "repo": "registry.hub.docker.com/linuxserver/wireguard",
                "tag": "latest",
                "sha256": "ae353ed4fa1a0c93b838c62c0883edf6727c24e3f081d75f0dacb0ae6b37fb8a"
            }
        },
        "edge": {
            "groundseg": {
                "major": 1,
                "minor": 0, 
                "patch": 8,
                "amd64_url": "https://bin.infra.native.computer/groundseg_amd64_edge",
                "arm64_url": "https://bin.infra.native.computer/groundseg_arm64_edge",
                "amd64_sha256": "c170b2b5111ea7b88db798b0740fa8d3e3eeaa02f6b42c4fdda73a52cae7b969",
                "arm64_sha256": "769200017da12766728cab8f17bc11bbc4cd5a9540cc919b364649aa74cc2cdd"
            },
            "webui": {
                "repo": "registry.hub.docker.com/nativeplanet/groundseg-webui",
                "tag": "edge",
                "sha256": "3192699f1a69468b121d006eadde61026f2a149a6a4223602fb25464ae000a26"
            },
            "vere": {
                "repo": "registry.hub.docker.com/nativeplanet/urbit",
                "tag": "v1.20",
                "sha256": "16a1d2e80e4000555dd53a4e918ad72501f5bc827722fa113a348024f97d4a8f"
            },
            "minio": {
                "repo": "registry.hub.docker.com/minio/minio",
                "tag": "latest",
                "sha256": "a0a002cb113c3fc6b0a8d4a7a8ebaa8d151a734290db9f92a234b95573753aef"
            },
            "miniomc": {
                "repo": "registry.hub.docker.com/minio/mc",
                "tag": "latest",
                "sha256": "ad34abeba912fa92f3cc4b462d53370a2eab07c59ca7c9c851656972e3d42f84"
            },
            "wireguard": {
                "repo": "registry.hub.docker.com/linuxserver/wireguard",
                "tag": "latest",
                "sha256": "ae353ed4fa1a0c93b838c62c0883edf6727c24e3f081d75f0dacb0ae6b37fb8a"
            }
        }
    }
}
```