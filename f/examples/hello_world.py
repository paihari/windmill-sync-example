def main(name: str = "Nicolas Bourbaki"):
	print(f"Hello World and a warm welcome especially to Sync {name}")
	return {"len": len(name), "splitted": name.split() }