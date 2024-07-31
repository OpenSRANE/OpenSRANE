# /* ****************************************************************** **
# **   OpenSRANE - Open Software for Risk Assessment of Natech Events   **
# **                                                                    **
# **                                                                    **
# **                                                                    **
# ** (C) Copyright 2023, Mentioned Regents in 'COPYRIGHT' file.         **
# **                                                                    **
# ** All Rights Reserved.                                               **
# **                                                                    **
# ** Commercial use of this program without express permission of the   **
# ** owner (The Regents), is                                            **
# ** strictly prohibited.  See file 'COPYRIGHT'  in main directory      **
# ** for information on usage and redistribution,  and for a            **
# ** DISCLAIMER OF ALL WARRANTIES.                                      **
# **                                                                    **
# ** Developed by:                                                      **
# **   Bijan SayyafZadeh (OpenSRANE@Gmail.com)                          **
# **   MehDi Sharifi                                                    **
# **   Abdolreza S. Moghadam                                            **
# **   Eslam Kashi                                                      **
# **                                                                    **
# ** ****************************************************************** */

from setuptools import setup, find_packages

import subprocess
import os

OpenSRANE_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert "." in OpenSRANE_version

assert os.path.isfile("opensrane/version.py")
with open("opensrane/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{OpenSRANE_version}\n")



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="OpenSRANE",
    version=OpenSRANE_version,
    author="Bijan Sayyafzadeh",
    author_email="<OpenSRANE@Gmail.com>",
    description="Open System for Risk Assessment of Natech Events",
    long_description_content_type="text/markdown",
    long_description=long_description ,
    package_data={
        # "":["*.jpg","*.at2","*.pyd"],

    },
    packages=find_packages(),
    install_requires=['numpy','plotly','scipy','kaleido','tqdm','pandas','ipywidgets','nbformat','ipykernel','matplotlib'],
    url="https://github.com/OpenSRANE/OpenSRANE",
    keywords=['python', 'NaTech', 'Modeling', 'Risk'],
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows'
    ],

)
