from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT= '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads requirements.txt file and returns 
    the list of dependencies needed for setup.py.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines (\n) from each read package line
        requirements = [req.replace("\n", "") for req in requirements]

        # Ignore the local editable installation flag if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="MLOPS_Pipeline",
    version="0.0.1",
    author="Rambagaria",
    author_email="rambagaria@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    # install_requires=['pandas', 'numpy', 'scikit-learn', 'joblib', 'pytest','seaborn']
)