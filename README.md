# AWX-RPM

RPM builds of the AWX project (https://www.github.com/ansible/awx)

This project is NOT an official Ansible Project, but provides RPMs for the people that prefers this kind of deployment.

An ansible playbook for installation is provided in ansible/

Inventory can be configured in ansible/inventory and is documented within the file.

___

Update: 16-02-2024

* AWX-RPM 23.8.1 is out..

Updating should be as simple as:

- Changing the version in /etc/yum.repos.d/awx-rpm.repo to 23.8.1
- Running "dnf update awx-rpm"
- Running "awx-manage migrate"
- Running "systemctl restart awx-*"

Have fun

___

Update: 05-02-2024

* Release of version 23.7.0

___

Update: 10-01-2024

Release of 23.6.0

* Updating should now be as simple as changing the version in the ansible playbook, and rerunning the playbook (please report any issues)
* I only spent about 2 hours to get from 23.5.1 -> 23.6.0, so the building seems to be A LOT more stable and easy now..
* Only one package had to be fixed manually, aside from dependency fixing with the main AWX-RPM package (and a new package from the AWX team, django-ansible-base)
* I expect to be able to keep pretty close to the release of the AWX team from now on

Please start to break it :) 
___

Update: 09-01-2024

Build process of 23.6.0:

https://github.com/MrMEEE/awx-rpm-versions/tree/23.6.0

Documentation is also getting started..

I have removed quite a few bugs from the ansible installer, as well as the packages and NGINX configuration..

---

Update: 05-01-24

Well, well, well.. 23.5.1 went pretty smoothly with the new building stuff..

* Don't ask why the version is 23.5.2-*******

* The installer fails on the common awx.target systemd service (because I forgot to include it), but the rest works...

* I haven't tested updates (or pretty much anything else)..

* IT RUNS!!! :)

Test it, break it and report it :D.. 

---

Update: 31-12-2023

If anyone is interested in following the process of building version 23.5.1:

https://github.com/MrMEEE/awx-rpm-versions/tree/23.5.1

Here you can also try to help troubleshooting the individual package problems, and pull requests will be highly appreciated..

Happy New Year... one more time..

---

Update: 30-12-2023

After a year that has been full of changes, I have now finally been able to get most of the cleanup and rebuild stuff done..

I know it's an old release, but 21.12.0 should now be ready for testing: https://rpm.awx.wiki/AWX-RPM/awx-rpm-21.12.0.repo

My main focus now is to get the newest AWX version released (23.x.x) as soon as possible, and after that to get the build process documented, so that you guys can contribute, if you feel like it..

Happy new year...

---

Update: 27-04-2023

There are package dependency issues on updating, see issue #3..

To update, run "dnf update --nobest"

---

Update: 19-04-2023

Well, well, well..


Something is ready.. not sure I should call it Alpha, Beta or Release Candidate, but I'll let you guys be the judges of that :)


But AWX-RPM 21.11.0 is now available for install..


The install playbook is available in the repo:


https://github.com/MrMEEE/awx-rpm-v2/tree/main/ansible


So far I have only tested on RHEL9, but CentOS Stream 9 and other variants should work as well..


Setup the AWX-RPM admin user, email and password in the inventory file, along with the hostname/IP of the machine to install to, and run:


ansible-playbook -i inventory awx-rpm-install.yml


and soon you should have a running AWX-RPM..


The webinterface will be available at https://<hostname>:8043/


Please report any issues at: https://github.com/MrMEEE/awx-rpm-v2/issues


Have fun, and feel free to report any issues and send any pull requests that makes sense..

---

Update: 28-02-2023

Lets create a community :)

First of all.. AWX-RPM is NOT, and I repeat NOT ready yet.. but I would say that the packaging is close to completed, and now there are some different stuff left:

- Getting all the services running

- Getting the services to talk to eachother

- Documentation

- Testing

- Building/modifying tools (needed for runtimes/installation)

And I could use some help.. I have created a RPM repo (GPG key and repo-file is in the description):

https://rpm.awx.wiki/AWX-RPM/

Which should be able to install on RHEL9 (probably also other EL9 like Alma/Rocky/Stream)

The installation for now should be something like (if someone have the time todo a writeup/test, I would appreciate it): [INSTALL](INSTALL.md)

I will try to create issues for the stuff that I find which is not working, and then we can hopefully solve it from there..

Happy bug hunting...

----
AWX-RPM Reignited

Hi guys

It's been some time.. And I know that there have been a lot of promises, and few of them have been kept..

The AWX-RPM project is back under my wings, and I hope push out new builds as fast as I can..

Recent work from the CentOS community and Red hat has made dependency building A LOT easier.. it's not perfect yet (and probably never will be), but it will make maintenance of the RPMS a lot less time consuming.

Because of this I have decided to completely reignite the AWX-RPM project, scrap all the old work (but keep the know-how) and if you want to follow the progress, follow this new repo, which will also be where new issues can be reported in time..

Right now I'm trying to build something to handle dependency building and exceptions to the depbuilding process... this is about 80% of the work..

From there I'll create the AWX-RPM core and services files and at some point create an installer..

When the core and services files are done, I'll see the project as Beta and ready for testing.. I hope this will happen within february, but it all depends on work pressure and family, so have patience.

However, when this is done, I'm really confident that automatic builds should be rolling out without needing much effort from my side.

Thanks for all your patience, support and feedback.

Talk to you all soon..

**Install guide, tools, utilities will be located at: https://awx.wiki in time.. they are outdated for now

**LinkedIn group for Questions, support, talk and more: https://www.linkedin.com/groups/13694893/


-----------------------------------

scripts:
```
buildsrc: Build src.rpm packages for the generated spec files
changeversion: Change the AWX version we are working on
checkbuilds: Check status of builds
getsources: Get source files for generated spec files 
mockbuild: Build the generated src.rpm-files to rpms with mock
pypi2spec: Generate specfiles for the requirement files
single-mockbuild: (re)build a single build, also generating a new src.rpm before build the rpm
```
