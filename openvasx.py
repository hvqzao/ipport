#!/usr/bin/env python

# Wed Mar 18 16:39:27 CET 2015
#
# allows automated arrangement of scan tasks with ports specified

from lxml import etree
import subprocess

class Openvas (object):

    # default configs
    class config:
        DISCOVERY='Discovery'
        EMPTY='empty'
        FULL_AND_FAST='Full and fast'
        FULL_AND_FAST_ULTIMATE='Full and fast ultimate'
        FULL_AND_DEEP='Full and very deep'
        FULL_AND_DEEP_ULTIMATE='Full and very deep ultimate'
        HOST_DISCOVERY='Host Discovery'
        SYSTEM_DISCOVERY='System Discovery'

    openvas_error = ''

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def _openvas_send_xml (self,xml):
        cmd = ['omp','-h',self.host,'-p',str(self.port),'-u',self.username,'-w',self.password,'-X',xml]
        #print(' '.join(cmd))
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, openvas_error = p.communicate()
        return out

    @staticmethod
    def stringified_xml (xml):
        ''' remove unnecessary blanks from xml '''
        p = etree.XMLParser(remove_blank_text=True)
        e = etree.XML(xml, parser=p)
        return etree.tostring(e)

    @staticmethod
    def pretty_xml (xml):
        return etree.tostring(etree.fromstring(xml),pretty_print=True)

    def create_port_list (self,name,tcp='',udp='',comment=''):
        if isinstance(tcp,list):
            tcp = ','.join(map(lambda x: str(x), tcp))
        if isinstance(udp,list):
            udp = ','.join(map(lambda x: str(x), udp))
        xml = '''\
<create_port_list>
    <name>'''+name+'''</name>
    <comment>'''+comment+'''</comment>
    <port_range>'''+['','T:'+tcp][tcp != '']+['',','][tcp != '' and udp != '']+['','U:'+udp][udp != '']+'''</port_range>
</create_port_list>'''
        return self._openvas_send_xml (self.stringified_xml (xml))

    def get_port_list_xml (self, pretty_print=False):
        xml = '<get_port_lists/>'
        result = self._openvas_send_xml (self.stringified_xml (xml))
        if pretty_print:
            return self.pretty_xml (result)
        else:
            return result

    def delete_check_uuid (func):
        def wrapped (self,uuid,*args,**kwargs):
            if uuid:
                return func (self,uuid,*args,**kwargs)
            else:
                return '<'+func.__name__+' status_text="UUID=None" status="400"></'+func.__name__+'>'
        return wrapped

    @delete_check_uuid
    def delete_port_list (self,uuid):
        return self._openvas_send_xml ('<delete_port_list port_list_id="'+uuid+'"/>')

    @staticmethod
    def _get_uuid (name, node, xml):
        e = etree.fromstring(xml)
        for i in e.xpath('//'+node):
            uuid = i.attrib['id']
            n = i.xpath('./name')[0].text
            if n == name:
                return uuid
        return None

    def get_port_lists_uuid (self, name, xml=None):
        if xml == None:
            xml = self.get_port_list_xml()
        return self._get_uuid (name,'port_list',xml)

    def create_target (self, name, hosts, port_list_uuid=None):
        xml = '''\
<create_target>
    <name>'''+name+'''</name>
    <hosts>'''+hosts+'''</hosts>'''+['','''
    <port_list id="'''+str(port_list_uuid)+'''"/>'''][port_list_uuid != None]+'''
</create_target>'''
        return self._openvas_send_xml (xml)

    def get_targets_xml (self, pretty_print=False):
        xml = '<get_targets/>'
        result = self._openvas_send_xml (self.stringified_xml (xml))
        if pretty_print:
            return self.pretty_xml (result)
        else:
            return result

    def get_target_uuid (self, name, xml=None):
        if xml == None:
            xml = self.get_targets_xml()
        return self._get_uuid (name,'target',xml)

    @delete_check_uuid
    def delete_target (self,uuid):
        return self._openvas_send_xml ('<delete_target target_id="'+uuid+'"/>')

    def get_scan_configs_xml (self, pretty_print=False):
        xml = '<get_configs/>'
        result = self._openvas_send_xml (self.stringified_xml (xml))
        if pretty_print:
            return self.pretty_xml (result)
        else:
            return result

    @staticmethod
    def _get_list (node, xml):
        e = etree.fromstring(xml)
        r = []
        for i in e.xpath('//'+node):
            #uuid = i.attrib['id']
            n = i.xpath('./name')[0].text
            r += [n]
        return r

    def get_scan_configs_list (self, xml=None):
        if xml == None:
            xml = self.get_scan_configs_xml()
        return self._get_list ('config',xml)

    def get_scan_config_uuid (self, name, xml=None):
        if xml == None:
            xml = self.get_scan_configs_xml()
        return self._get_uuid (name,'config',xml)

    def get_tasks_xml (self, pretty_print=False):
        xml = '<get_tasks/>'
        result = self._openvas_send_xml (self.stringified_xml (xml))
        if pretty_print:
            return self.pretty_xml (result)
        else:
            return result

    def get_task_list (self, xml=None):
        if xml == None:
            xml = self.get_tasks_xml()
        return self._get_list ('task',xml)

    def get_task_uuid (self, name, xml=None):
        if xml == None:
            xml = self.get_tasks_xml()
        return self._get_uuid (name,'task',xml)

    def create_task (self, name, target, scan_config):
        if self.get_task_uuid (name=name):
            return '<create_task status_text="Task with this name exists already" status="400"></create_task>'
        xml = '''\
<create_task>
   <name>'''+name+'''</name>
   <config id="'''+scan_config+'''"/>
   <target id="'''+target+'''"/>
 </create_task>'''
        return self._openvas_send_xml (xml)

    @delete_check_uuid
    def delete_task (self, uuid):
        return self._openvas_send_xml ('<delete_task task_id="'+uuid+'"/>')


if __name__ == '__main__':

    # Example usage

    tcp = [80,443,7501,10001]
    ip = '127.0.0.1'
    name = 'tag-'+ip

    openvas = Openvas (host='localhost', port=9390, username='api', password='*****')

    # create port_list
    print(openvas.create_port_list (name=name,tcp=tcp))
    # print(port_list xml)
    print(openvas.get_port_list_xml (pretty_print=True))
    # get port_list uuid for given name
    print(openvas.get_port_lists_uuid (name=name))

    # create target
    print(openvas.create_target (name=name,hosts=ip,port_list_uuid=openvas.get_port_lists_uuid (name=name)))
    # will not work (duplicate name not allowed by this API)
    print(openvas.create_target (name=name,hosts=ip,port_list_uuid=openvas.get_port_lists_uuid (name=name)))
    # print(targets xml)
    print(openvas.get_targets_xml (pretty_print=True))
    # get target uuid for given name
    print(openvas.get_target_uuid (name=name))

    # get scan configs xml 
    print(openvas.get_scan_configs_xml (pretty_print=True))
    # get scan configs list
    print(openvas.get_scan_configs_list())
    # get scan_config uuid for given name
    print(openvas.get_scan_config_uuid (openvas.config.FULL_AND_FAST))
    # get tasks xml
    print(openvas.get_tasks_xml (pretty_print=True))
    # create task
    print(openvas.create_task (name=name, target=openvas.get_target_uuid (name=name), scan_config=openvas.get_scan_config_uuid (openvas.config.FULL_AND_FAST)))
    # get task list
    print(openvas.get_task_list())
    # get task uuid for given name
    print(openvas.get_task_uuid (name=name))

    # delete task
    print(openvas.delete_task (uuid=openvas.get_task_uuid (name=name)))

    # delete target
    print(openvas.delete_target (openvas.get_target_uuid (name=name)))

    # delete port_list
    print(openvas.delete_port_list (openvas.get_port_lists_uuid (name=name)))

    # will not work (UUID=None)
    print(openvas.delete_task (uuid=openvas.get_task_uuid (name=name)))
    print(openvas.delete_target (openvas.get_target_uuid (name=name)))
    print(openvas.delete_port_list (openvas.get_port_lists_uuid (name=name)))
