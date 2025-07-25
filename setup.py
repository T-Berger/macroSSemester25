import setuptools 

with open("README.md", "r", encoding="utf-8") as fh: 
   long_description = fh.read()
 
setuptools.setup(
   name = "Macromedia-demo-pkg-2022",
   version = "0.0.1",
   author = "Macromedia Prof",
   author_email = "author@example.com",
   description = "Ein kleines Beispielpaket",
   long_description = long_description,
   long_description_content_type = "text/markdown",
   url = "https://github.com/pypa/macromediasampleproject",
   project_urls = {
      "Bug Tracker": "https://github.com/pypa/macromediasampleproject/issues",
   },
   classifiers = [
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
   package_dir = {"": "src"},
   packages = setuptools.find_packages(where = "src"),
   python_requires = ">=3.6", 
) 
 