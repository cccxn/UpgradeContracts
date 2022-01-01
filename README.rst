Upgrade Contracts
----------------
- brownie init ;
- touch README.rst ;
- For the Brownie Bake ;
    - brownie bake upgrades-mix ;
    - mv upgrades JUNK ;
Git Set-Up
==========
- git init ;
- git config --global user.name "myname" ;
- git config --global user.email "myname@email.com" ;
- git commit -m "Initial Commit" ;
- git branch -M master ;
- git remote add origin https://github.com/XXXXXX/UpgradeContracts.git
- git push -u origin master ;

Start the Work
==============
- brownie compile ;
- test_box_proxy.py ;
- brownie test -k test_proxy_upgrades ;