NUMPY_MIN_VERSION = "1.19.0"
SCIPY_MIN_VERSION = "1.1.0"
PYTEST_MIN_VERSION = "5.0.1"

dependent_packages = {
    "numpy": (NUMPY_MIN_VERSION, "build, install"),
    "scipy": (SCIPY_MIN_VERSION, "build, install"),
    "pytest": (PYTEST_MIN_VERSION, "tests"),
}

tag_to_packages: dict = {
    extra: []
    for extra in ["build", "install", "tests"]
}
for package, (min_version, extras) in dependent_packages.items():
    for extra in extras.split(", "):
        tag_to_packages[extra].append(f"{package}>={min_version}")
