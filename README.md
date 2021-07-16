# MyLeagueManager

MyLeagueManager is a sport league management application, which allows users to create and delete leagues, as well as simulate seasons of play. 
The application achieves this by leveraging the file system for reading/writing data. Deployment support to multiple virtual machines is automated, 
including configuration of a virtual environment, installation, launching, retrieval of program logs, and uninstallation.

Playbooks should be run in the order of :
  setup_env.yaml - to set up environment needed to install/launch application
  git_checkoutProj0.yaml - checkout most recent version of project from Git
  run_proj0.sh - bash script to run application
  get_proj0_log.yaml - gets any logs produced by application
  uninstall_Proj0.yaml - uninstalls application


Application can be launched with the proj0.py file.  Logs are saved within the gamefiles directory.
