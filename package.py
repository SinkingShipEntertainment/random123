name = "random123"

authors = [
    "John Salmon",
    "Mark Moraes",
]

# NOTE: version = <usd_version>.sse.<sse_version>
version = "1.14.0.sse.2.0.0"

description = \
    """
    C++ random numbers
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"
uuid = "repository.random123"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.RANDOM123_VERSION = external_version
    env.RANDOM123_PACKAGE_VERSION = external_version
    if internal_version:
        env.RANDOM123_PACKAGE_VERSION = internal_version

    env.RANDOM123_ROOT.append("{root}")
    env.RANDOM123_LOCATION.append("{root}")
    env.RANDOM123_INCLUDE_DIR = "{root}/include"
