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

The installation for now should be something like (if someone have the time todo a writeup, I would appreciate it):

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
