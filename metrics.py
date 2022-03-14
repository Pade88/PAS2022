import os
import subprocess


def mc_cabe():
	if "McCabe" not in os.listdir(os.getcwd()):
		os.mkdir("McCabe")

	for file in os.listdir(os.getcwd()):
		if file.split(".")[-1] == "py":
			with open(f'McCabe/{file.split(".")[0]}.txt', "w+") as outputfile:
				outputfile.write(subprocess.check_output(["python3", "-m", "mccabe", file]).decode())


def multi_metric():
	if "MultiMetric" not in os.listdir(os.getcwd()):
		os.mkdir("MultiMetric")

	for file in os.listdir(os.getcwd()):
		if file.split(".")[-1] == "py":
			with open(f'MultiMetric/{file.split(".")[0]}.json', "w+") as outputfile:
				outputfile.write(subprocess.check_output(["multimetric", file]).decode())


if __name__ == "__main__":
	mc_cabe()
	multi_metric()