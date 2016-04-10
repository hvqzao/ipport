Setup assumes https://github.com/hvqzao/x is set up in /root/x directory.

Usage:

Install docker:

```sh
sudo aptitude install docker.io
```

Build kali-linux docker image and dependent ipport image:

```sh
git submodule update --init --recursive
./kali-linux-docker/build.sh
./build.sh
```

Start container:

```sh
./run some-temporary-container-name
```
