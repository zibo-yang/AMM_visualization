# AMM_visualization
AMM_visualization contains authur's programs to visualize the decentralized exchange of automated market maker. You could find explanation of this concepts below.

##Installation
In order to compile, please install matplotlib and python3 first:
'''bash
python -m pip install -U pip
python -m pip install -U matplotlib
''' 

##Usage
'''bash
cd src/
python3 main.py
'''

##Introduction of AMM
An automated market maker (AMM) is a type of decentralized exchange (DEX) protocol that relies on a mathematical formula to price assets.
//picture

Most of AMM uses x * y = k, where x is the amount of one token in the liquidity pool, and y is the amount of the other. In this formula, k is a fixed constant, meaning the pool’s total liquidity always has to remain the same. 
//picture

What authur programmed here is the complex version of AMM with formula changed to:
$$x*y + z(x + y) = k$$


