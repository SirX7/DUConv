import sys
from getopt import getopt, GetoptError

from duconv import bytesconvert
from duconv import convert
from duconv import __version__ as _v

HELPER = f"run the command with the -h or --help option to recieve help"


def help() -> str:
    """Prints usage for when running as a cli app."""

    usage = f"""HELP:\nDESCRIPTION\nThis is a package that can be run from the cli to help in converting digital data units.
COMMANDS
Usage:duconv [-bdgkmthv] [--byte] [--data-to-byte] [--kb] [--mb] [--gb] [--tb] [--help] [--version]
-b, --byte\t\tConvert bytes to KB, MB, GB, and TB
-d, --data-tobyte\tConvert KB, MB, GB, and TB to bytes
-k, --kb\t\tConvert MB, GB, and TB to KB
-m, --mb\t\tConvert KB, GB, and TB to MB
-g, --gb\t\tConvert KB, MB, and TB to GB
-t, --tb\t\tConvert KB, MB, and GB to TB
-v, --version\t\tShow the version
-h, --help\t\tShow usage.
    
e.g: to convert 5 MB in to KB you ust run:
     
     duconv [-k | --kb] 5 M

usable e.g:1
    
     duconv -k 5 M

to convert bytes to KB, MB, GB, TB run:
    
     duconv -b 5000

for other conversion see usable e.g:1
"""

    return usage


def cli() -> None:
    cliArg = sys.argv[1:]
    shortOpt = "b:d:k:m:g:t:vh"
    longOption = [
        "byte=",
        "data-to-byte=",
        "kb=",
        "mb=",
        "gb=",
        "tb=",
        "help",
        "version",
    ]

    try:
        opts, args = getopt(cliArg, shortOpt, longOption)

    except GetoptError as error:
        print(f"{error}\n{HELPER}")

    else:
        if len(opts) < 1:
            print("no options was given")
            sys.exit(f"{HELPER}\nexit code=1")

        for opt, val in opts:
            try:
                if opt in ("-b", "--byte"):
                    print(bytesconvert.bytes_converter(float(val)))

                elif opt in ("-d", "--data-to-byte"):
                    print(bytesconvert.data_to_bytes(float(val), args[0]))

                elif opt in ("-k", "--kb"):
                    print(convert.to_kb(float(val), args[0]))

                elif opt in ("-m", "--mb"):
                    print(convert.to_mb(float(val), args[0]))

                elif opt in ("-g", "--gb"):
                    print(convert.to_gb(float(val), args[0]))

                elif opt in ("-t", "--tb"):
                    print(convert.to_tb(float(val), args[0]))

                elif opt in ("-h", "--help"):
                    print(help())

                elif opt in ("-v", "--version"):
                    print(
                        f"duconv version {_v}\n\nCopyright 2023 Shall Mcfield.\nLicense under the MIT License"
                    )

            except (ValueError, Exception) as e:
                sys.exit(f"{HELPER}\nnumeric value required (exit code=1)")


if __name__ == "__main__":
    cli()
