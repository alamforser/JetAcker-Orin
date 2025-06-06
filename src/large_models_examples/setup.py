import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'large_models_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
        (os.path.join('share', package_name, 'large_models_examples'), glob(os.path.join('large_models_examples', '*.*'))),
        (os.path.join('share', package_name, 'large_models_examples', 'navigation_transport'), glob(os.path.join('large_models_examples', 'navigation_transport', '*.*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='1270161395@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'llm_control_move = large_models_examples.llm_control_move:main',
            'llm_color_track = large_models_examples.llm_color_track:main',
            'llm_visual_patrol = large_models_examples.llm_visual_patrol:main',
            'navigation_controller = large_models_examples.navigation_controller:main',
            'automatic_pick = large_models_examples.navigation_transport.automatic_pick:main',
            'vllm_with_camera = large_models_examples.vllm_with_camera:main',
            'vllm_track = large_models_examples.vllm_track:main',
            'vllm_navigation = large_models_examples.vllm_navigation:main',
            'vllm_navigation_transport = large_models_examples.navigation_transport.vllm_navigation_transport:main',
        ],
    },
)
