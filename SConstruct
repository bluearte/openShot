import sconsutils

env = sconsutils.configure()

openShot = env.make_install(name="openShot",
                            app="nuke",
                            version="0.1.0",
                            verfiles={"python/openShot_version.py": None},
                            install_files={"python/*.py": "all/python",
                                           "release.txt": "../all/all"},
                            template="openShot.template")
