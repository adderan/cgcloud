from cgcloud.core.generic_boxes import *
from cgcloud.bd2k.ci.generic_jenkins_slaves import UbuntuTrustyGenericJenkinsSlave
from fabric.operations import run, put, os
from cgcloud.fabric.operations import sudo, remote_open
from cgcloud.core import fabric_task
from fabric.context_managers import settings

class UbuntuCactusBuild( UbuntuTrustyGenericJenkinsSlave ):
    """
    For building progressiveCactus. Creates a statically-linked tar which
    is sent to the Cactus benchmark and test server.
	"""
    def __init__( self, ctx ):
        super( UbuntuCactusBuild, self ).__init__(ctx)

    def _list_packages_to_install( self ):
        return super( UbuntuCactusBuild, self)._list_packages_to_install() + [
                'python-dev' ]

    @fabric_task
    def _setup_build_user(self):
        super( UbuntuCactusBuild, self)._setup_build_user()
        sudo( "ln -s /usr/lib/python2.7/plat-*/_sysconfigdata_nd.py /usr/lib/python2.7/" )


    #def _post_install_pacakges( self ):
    #    super ( UbuntuCactusBuild, self)._post_install_packages( )
    #    self.__fix_python_installation( )
		
    #@fabric_task
    #def __fix_python_installation( self ):
    #    sudo( "ln -s /usr/lib/python2.7/plat-*/_sysconfigdata_nd.py /usr/lib/python2.7/" )
