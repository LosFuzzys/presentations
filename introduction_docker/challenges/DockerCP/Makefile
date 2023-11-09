

all:
	cython execute.py --embed
	PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags) gcc -Os $(python3-config --includes) execute.c -o output_bin_file $(python3-config --ldflags) -l$PYTHONLIBVER