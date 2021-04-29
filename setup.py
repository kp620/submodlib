from glob import glob
from setuptools import find_packages, setup
import sys

try:
    from pybind11.setup_helpers import Pybind11Extension, build_ext
except ImportError:
    from setuptools import Extension as Pybind11Extension


with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('submodlib/version.py').read())

ext_modules = [
    Pybind11Extension("submodlib_cpp",
        ["cpp/SetFunction.cpp",
        "cpp/utils/helper.cpp", "cpp/wrappers/wr_helper.cpp",
        "cpp/utils/sparse_utils.cpp", "cpp/wrappers/wr_sparse_utils.cpp",
        "cpp/optimizers/NaiveGreedyOptimizer.cpp", 
        "cpp/optimizers/LazyGreedyOptimizer.cpp", 
        "cpp/optimizers/StochasticGreedyOptimizer.cpp", 
        "cpp/optimizers/LazierThanLazyGreedyOptimizer.cpp", 
        "cpp/wrappers/wrapper.cpp", 
        "cpp/submod/FacilityLocation.cpp", "cpp/wrappers/wr_FacilityLocation.cpp", 
        "cpp/submod/DisparitySum.cpp", "cpp/wrappers/wr_DisparitySum.cpp", 
        "cpp/submod/FeatureBased.cpp", "cpp/wrappers/wr_FeatureBased.cpp", 
        "cpp/submod/GraphCut.cpp", "cpp/wrappers/wr_GraphCut.cpp", 
        "cpp/submod/SetCover.cpp", "cpp/wrappers/wr_SetCover.cpp", 
        "cpp/submod/ProbabilisticSetCover.cpp", "cpp/wrappers/wr_ProbabilisticSetCover.cpp", 
        "cpp/submod/DisparityMin.cpp", "cpp/wrappers/wr_DisparityMin.cpp", 
        "cpp/submod/LogDeterminant.cpp", "cpp/wrappers/wr_LogDeterminant.cpp", 
        "cpp/smi/FacilityLocationMutualInformation.cpp", "cpp/wrappers/wr_FacilityLocationMutualInformation.cpp", 
        "cpp/smi/FacilityLocationVariantMutualInformation.cpp", "cpp/wrappers/wr_FacilityLocationVariantMutualInformation.cpp", 
        "cpp/smi/ConcaveOverModular.cpp", "cpp/wrappers/wr_ConcaveOverModular.cpp", 
        "cpp/smi/GraphCutMutualInformation.cpp", "cpp/wrappers/wr_GraphCutMutualInformation.cpp", 
        "cpp/condgain/GraphCutConditionalGain.cpp", "cpp/wrappers/wr_GraphCutConditionalGain.cpp", 
        "cpp/smi/MutualInformation.cpp", 
        "cpp/smi/LogDeterminantMutualInformation.cpp", "cpp/wrappers/wr_LogDeterminantMutualInformation.cpp", 
        "cpp/Clustered.cpp", "cpp/wrappers/wr_Clustered.cpp"],
        # Example: passing in the version to the compiled code
        #sorted(glob("cpp/submod/*.cpp")),
        define_macros = [('VERSION_INFO', __version__)],
        ),
]


setup(
    name='submodlib',
    #packages=find_packages(include=['submodlib']),
    packages=['submodlib', 'submodlib/functions'],
    #packages=find_packages('submodlib'),
    #package_dir={'':'submodlib'},
    #version='0.0.2',
    version=__version__,
    description='submodlib is an efficient and scalable library for submodular optimization which finds its application in summarization, data subset selection, hyper parameter tuning etc.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vishal Kaushal',
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    author_email='vishal.kaushal@gmail.com',
    url="https://github.com/vishkaush/submodlib",
    #url='http://pypi.python.org/pypi/submodlib/',
    #url="https://github.com/pypa/sampleproject",
    license='MIT',
    # install_requires=[
    #     "numpy >= 1.14.2",
    #     "scipy >= 1.0.0",
    #     "numba >= 0.43.0",
    #     "tqdm >= 4.24.0",
    #     "nose"
    # ],
    install_requires=[],
    setup_requires=['pybind11','pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    #classifiers=[
    #    "Programming Language :: Python :: 3",
    #    "License :: OSI Approved :: MIT License",
    #    "Operating System :: OS Independent",
    #],
    zip_safe=False 
)