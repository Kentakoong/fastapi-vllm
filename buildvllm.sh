apt-get update  -y
apt-get install -y gcc-12 g++-12 libnuma-dev python3-dev
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12

git clone https://github.com/vllm-project/vllm.git vllm_source

cd vllm_source

pip install --upgrade pip
pip install "cmake>=3.26" wheel packaging ninja "setuptools-scm>=8" numpy
pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

env VLLM_TARGET_DEVICE=cpu python setup.py install 

cd ..