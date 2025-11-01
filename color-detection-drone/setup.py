from setuptools import setup, find_packages

setup(
    name='color-detection-drone',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A drone project that integrates color detection and movement control using a GUI.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'opencv-python',
        'opencv-python-headless',
        'numpy',
        'PyQt5',  # or any other GUI framework you choose
        'torch',  # if using YOLO with PyTorch
        'torchvision',  # if using YOLO with PyTorch
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'color-detection-drone=main:main',  # Adjust according to your main function location
        ],
    },
)