# Machine configuration

The current configuration of the machine running this module is fully described in the files `distributions.txt` and `installed_programs.txt`

These files were created using the following system dumps:

* `dpkg -l >> distributions.txt`


* `compgen -c >> installed_programs.txt`

To replicate the configuration in your machine, run:

```bash
sudo dpkg --clear-selections
sudo dpkg --set-selections < programs_to_install.txt
sudo apt-get --reinstall dselect-upgrade
```
