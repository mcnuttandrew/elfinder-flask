'''
Comments are taken from https://github.com/Studio-42/elFinder/wiki/Client-Server-API-2.1
on 11/11/2019
'''

from felfinder.models import db

class ElFinderConnector():
    _version = '2.1'





































    def abort(self, aid):

        """
        Abort the specified request

        Arguments:

          aid : request id to abort

        Response: 

          Empty content with HTTP response code "204 No Content"

        """
        
        pass


    def archive(self, name, mimetype, target, targets):

        """
        Packs directories / files into an archive.

        Arguments:

          name : file name of the archive to create
          mimetype : mime-type for the archive
          target : hash of the directory that are added to the archive directories / files
          targets[] : an array of hashes of the directories / files to archive

        Response:

          added : (Array) Information about File/Directory of a new archive

        """

        pass

    def callback(self, node, json, bind, done):

        """
        Output callback result with JavaScript that control elFinder or HTTP redirect to 
        callback URL. This is used for communication with the outside, such as OAuth of netmount.

        Arguments:

          node : elFinder node DOM id that accepted /^[a-zA-Z0-9;._-]+$/ only
          json : JSON data for output
          bind : bind command name (optional)
          done : 1 or 0 - 0: output redirect HTTP response, 1: output HTML 
                 included JavaScript for IFRAME/Child Window.

        Response:

          HTTP response Location: 
            [Redirect URL(Defined in the volume driver)]?node={node}&json={json}&bind={bind}&done=1*
          
          HTML included JavaScript for IFRAME/Child Window Must  
          replace {$node}, {$bind}, {$json} for each value.

        """
        pass

    def chmod(self, targets, mode):

        """
        chmod target items.

        Arguments:

          targets[] : array of hashed paths of the nodes
          mode : Numeric notation file system permissions

        Response: 
          
          An array of successfully uploaded files if success, an error otherwise.

        changed : 
          (Array) of files that were successfully done chmod. Information about File/Directory
        
        """

        pass

    def dim(self, target, substitute):

        """
        Returns the dimensions of an image/video

        Arguments:

          target : hash path of the node
          substitute : pixel that requests substitute image (optional) - API >= 2.1030

        Response:

          dim: The dimensions of the media in the format {width}x{height} (e.g. "640x480").
          url: The URL of requested substitute image. (optional)


        """

        pass

    def duplicate(self, current, target):

        """
        Creates a copy of the directory / file. Copy name is generated as follows: 
        basedir_name_filecopy+serialnumber.extension (if any)

        Arguments:

          current : hash of the directory in which to create a duplicate
          target : hash of the directory / file that is being duplicated

        Response:
 
          added (Array) Information about File/Directory of the duplicate.

        """

        pass

    def editor(self, cmd, name, method, args):

        """


        """

        pass

    def extract(self, target, makedir):

        """

        Unpacks an archive.

        Arguments:

          cmd : extract
          target : hash of the archive file
          makedir : "1" to extract to new directory

        Response:

          added : (Array) Information about File/Directory of extracted items

        """
        pass

    def file(self, target, download, cpath):

        """

        Output file into browser. This command applies to download and preview actions.

        Arguments:

          cmd : file
          target : file's hash,
          download : Send headers to force download file instead of opening it in the browser.
          cpath (API >= 2.1.39) : Cookie path that temporary cookie set up until download starts. 
                                  If this parameter is specified, the connector must set the 
                                  cookie name as "elfdl" + Request ID (The value is irrelevant, 
                                  maybe "1") . This cookie is deleted by the client at the start 
                                  of download.


        May need to set Content-Disposition, Content-Location and Content-Transfer-Encoding. 
        Content-Disposition should have 'inline' for preview action or 'attachments' for download.

        """

        pass

    def get(self, current, target, conv):

        """

        Returns the content as String (As UTF-8)

        Arguments:

          current : hash of the directory where the file is stored
          target : hash of the file
          conv : instructions for character encoding conversion of the text file
                   1 : auto detect encoding(Return false as content in response data when failed)
                   0 : auto detect encoding(Return { "doconv" : "unknown" } as response 
                       data when failed)

                   Original Character encoding : original character encoding as 
                                                 specified by the user

        Response:

          content: file contents (UTF-8 String or Data URI Scheme String) or false
          encoding: (Optional) Detected original character encoding 
                               (Require when converting from encoding other than UTF-8)
          doconv: (Optional) "doconv":"unknown" is returned to ask the user for the original 
                              encoding if automatic conversion to UTF-8 is not possible 
                              when requested with conv = 0.

        """

        pass

    def info(self, targets):

        """

        Returns information about places nodes

        Arguments:

          targets[] : array of hashed paths of the nodes

        Response:

          files: (Array of data) places directories info data Information about File/Directory

        """

        pass

    def ls(self, target, intersect):

        """
        Return a list of item names in the target directory. 

        Arguments:

          target : hash of directory,
          intersect[] : An array of the item names for presence check.

        Response:

          list : (Object) item names list with hash as key. Return only duplicate files 
                          if the intersect[] is specified.
        
        """

        pass

    def mkdir(self, target, name, dirs):

        """
        Create a new directory.

        Arguments:

          target : hash of target directory,
          name : New directory name
          dirs[] : array of new directories path (requests at pre-flight of folder upload)

        Response:

          added : (Array) Array with a single object - a new directory. 
          hashes : (Object) Object of the hash value as a key to the given path in the dirs[]

        """


        pass

    def mkdfile(self, target, name):

        """
        Create a new blank file.

        Arguments:

          target : hash of target directory,
          name : New file name

        Response:

          added : (Array) Array with a single object - a new file. Information about File/Directory
        
        """
        pass

    def netmount(self, protocol, host, path, port, user, passw, alias, options):

        """

        Mount network volume during user session.

        Arguments:

          protocol : network protocol. Now only ftp supports. Required.
          host : host name. Required.
          path : root folder path.
          port : port.
          user : user name. Required.
          pass : password. Required.
          alias : mount point name. For future usage. Now not used on client side.
          options : additional options for driver. For future usage. Now not used on client side.


        """

        pass

    def open(self, target = '/', tree = False, init = False):

        """

        Returns information about requested directory and its content, optionally 
        can return directory tree as files, and options for the current volume.

        Arguments:

          init : (true|false|not set), optional parameter. If true indicates that this 
                 request is an initialization request and its response must include the value api 
                 (number or string >= 2) and should include the options object, but will still 
                 work without it. Also, this option affects the processing of parameter target 
                 hash value. If init == true and target is not set or that directory doesn't 
                 exist, then the data connector must return the root directory of the default 
                 volume. Otherwise it must return error "File not found".
          target : (string) Hash of directory to open. Required if init == false or init is not set
          tree : (true|false), optional. If true, response must contain the top-level 
                 object of other volumes.
        
        Response:

          api : (Float) The version number of the protocol, must be >= 2.1, 
                        ATTENTION - return api ONLY for init request!
          cwd : (Object) Current Working Directory - information about the current directory. 
                         Information about File/Directory
          files : (Array) array of objects - files and directories in current directory. If 
                          parameter tree == true, then added to the root folder objects of other 
                          volumes. The order of files is not important. Information about 
                          File/Directory
          netDrivers : (Array) Network protocols list which can be mounted on the fly 
                               (using netmount command). Now only ftp supported.

        
          uplMaxFile : (Optional) (Number) Allowed upload max number of file per request (e.g. 20)
          uplMaxSize : (Optional) (String) Allowed upload max size per request. (e.g. "32M")
          options : (Optional) (Object) Further information about the folder and its volume

        """


        basic = {"name" : "Boggle",
                 "hash"   : "l0_SW1hZ2Vz",
                 "mime"   : "directory",
                 "ts"     : 1334163643, 
                 "size"   : 12345,
                 "dirs"   : 0,
                 "read"   : 1,
                 "write"  : 1,
                 "locked" : 0,
                 "isowner": True,
                 "volumeid" : "l1_",
                 "options" : {}}

        cab = {"name" : "Scrabble",
               "hash"   : "l0_pXXUin",
               "mime"   : "directory",
               "ts"     : 1334163643, 
               "size"   : 12345,
               "dirs"   : 0,
               "read"   : 1,
               "write"  : 1,
               "locked" : 0,
               "isowner": True,
               "volumeid" : "l2_",
               "options" : {}}

        

        n = {"name" : "butter",
             "hash"   : "l1_abc",
             "phash"  : "l0_SW1hZ2Vz",
             "mime"   : "application/plain-text",
             "ts"     : 1334163643,
             "size"   : 12345,
             "read"   : 1,
             "write"  : 1,
             "locked" : 0,
             "isowner": True,
             "options" : {'disabled': []}}

        
        resp = {'api': 2.1,
                'cwd': basic,
                'files': [basic, cab, n],
                'netDrivers': ['ftp'],
                'options': {}}

        return resp


    def parents(self, target, until):

        """

        Returns all parent folders and their's first level (at least) subfolders and own(target) 
        stat. This command is invoked when a folder is reloaded or there is no data to display the 
        tree of the target folder in the client. Data provided by 'parents' command should enable 
        the correct drawing of tree hierarchy directories.

        Arguments:

          target : folder's hash
          until : until to hash, getting parents is enough for that (API >= 2.1024)

        Response:

          tree : (Array) Folders list

        """

        pass


    def paste(self, dst, targets, cut, renames, suffix):

        """

        Copies or moves a directory / files

        Arguments:
        
          dst : hash of the directory to which the files will be copied / moved (the destination)
          targets[] : An array of hashes for the files to be copied / moved
          cut : 1 if the files are moved, missing if the files are copied
          renames[] : Filename list of rename request
          suffix : Suffixes during rename (default is "~")

        Response:

          If the copy / move is successful:

            added : (Array) array of file and directory objects pasted. 
                            Information about File/Directory
            removed : (Array) array of file and directory 'hashes' that were successfully deleted

        """

        pass

    def ping(self):

        """
        Not currently used
        """

        raise NotImplementedError()

    def put(self, target, content, encoding):

        """

        Stores contents data in a file.

        Arguments:

          target : hash of the file
          content : new contents of the file
          encoding : character encoding at the time of saving (Text data will be sent by UTF-8) 
                     or "scheme" for URL of contents or Data URI scheme

        content of file data other than text file is sent as string data of Data URI Scheme or 
        URL of new contents with param encoding=scheme.

        Response: 

          changed : (Array) of files that were successfully uploaded.

        """

        pass

    def rename(self):

        """

        Renaming a directory/file

        Arguments:

          cmd : rename
          target : hash directory/file renaming
          name : New name of the directory/file

        Response:

          added : (Array) array of file and directory objects renamed. 
                          Information about File/Directory
          removed : (Array) array of file and directory 'hashes' that were successfully remoevd

        """

        pass

    def resize(self, mode, target, width, height, x, y, degree, quality):

        """

        Change the size of an image.

        Arguments:

          mode : 'resize' or 'crop' or 'rotate'
          target : hash of the image path
          width : new image width
          height : new image height
          x : x of crop (mode='crop')
          y : y of crop (mode='crop')
          degree : rotate degree (mode='rotate')
          quality: (unknown)

        Response:

          changed : (Array) of files that were successfully resized.

        """
        
        pass

    def rm(self, targets):

        """

        Recursively removes files and directories.

        Arguments:

          targets[] : (Array) array of file and directory hashes to delete

        Response:

          removed : (Array) array of file and directory 'hashes' that were successfully deleted

        """

        pass


    def search(self, q, target, mimes):

        """

        Return a list of files and folders list, that match the search string. arguments:

          q : search string
          target : search target hash (optional)
          mimes : Array of search target MIME-type (optional)

        Response:

          files : (Array) array of objects - files and folders list, that match the search string.

        """

        pass


    def size(self, targets):

        """

        Returns the size of a directory or file.

        Arguments:

          cmd : size
          targets[] : hash paths of the nodes

        Response:

          size: The total size for all the supplied targets.
          fileCnt: (Optional to API >= 2.1025) The total counts of the file for 
                                               all the supplied targets. 
          dirCnt: (Optional to API >= 2.1025) The total counts of the directory for 
                                              all the supplied targets. 
          sizes: (Optional to API >= 2.1030) An object of each target size infomation. 

        """


        pass

    def tmb(self, targets):

        """

        Background command. Creates thumbnails for images that do not have them. 
        Number of thumbnails created at a time is specified in the Connector_Configuration_RU 
        option tmbAtOnce. Default is 5.

        Arguments:

          targets[] : an array of hash path to the directory in which to create thumbnails

        Response:

          {'images': {'(hash_fpath)': '(thumbnail_url)'}}

        """


        pass

    def tree(self, target):

        """

        Return folder's subfolders.

        Arguments:

          cmd : tree
          target : folder's hash

        Response:

          tree : (Array) Folders list

        """

        pass

    def upload(self, target, upload, upload_path, mtime, name, renames, suffix, hashes, overwrite):

        """
        Process file upload requests. Client may request the upload of multiple files at once.

        Arguments:

          target : hash of the directory to upload
          upload[] : array of multipart files to upload
          upload_path[] : (optional) array of target directory hash, it has been a 
                                     pair with upload[]. (specified at folder upload)
          mtime[] : (optional) array of files UNIX time stamp, it has been a pair with upload[].
          name[] : (optional) array of files name for suggest, it has been a pair with upload[].
          renames[] : (optional) array of rename request filenames
          suffix : (optional) rename suffix
          hashes[hash] : (optional) array of hash: filename pairs
          overwrite : (optional) Flag to overwrite or save another name. If "0" is specified 
                                 and the same name file exists, the connector should save the 
                                 upload file as a different name.

        Response: 

          added : (Array) of files that were successfully uploaded.
        
        """

        pass

    def url(self, target, options):

        """

        Returns the url of a file. This method is called if the initial value for the 
        file's url is "1".

        Arguments:

          target : hash of file
          options[] : array of options (?)

        Response:

          url: url of the file

        """

        pass

    def zipdl(self):

        """
        Not implemented.
        """

        raise NotImplementedError()





    
        
    # def __init__(self, volumes={}):
    #     self.httpResponse = {}
    #     self.httpStatusCode = 200
    #     self.httpHeader = {'Content-type': 'application/json'}
    #     self.data = {}
    #     self.response = {}
    #     self.return_view = None

    #     # Populate the volumes dict, using volume_id as the key
    #     self.volumes = {}
    #     for volume in volumes:
    #         self.volumes[volume.get_volume_id()] = volume

    # def get_commands(self):
    #     """ Returns a dict which maps command names to functions.

    #         The dict key is the command name. The value is a tuple containing
    #         the name of a function on this class, and a dict specifying which
    #         GET variables must be set/unset. This lets us do validation of the
    #         given arguments, so the command functions can assume the correct
    #         values are set. Used by check_command_functions.
    #     """
    #     return {'open': ('__open', {'target': True}),
    #             'tree': ('__tree', {'target': True}),
    #             'file': ('__file', {'target': True}),
    #             'parents': ('__parents', {'target': True}),
    #             'mkdir': ('__mkdir', {'target': True, 'name': True}),
    #             'mkfile': ('__mkfile', {'target': True, 'name': True}),
    #             'rename': ('__rename', {'target': True, 'name': True}),
    #             'ls': ('__list', {'target': True}),
    #             'paste': ('__paste', {'targets[]': True, 'src': True,
    #                                   'dst': True, 'cut': True}),
    #             'rename': ('__rename', {'target': True, 'name': True}),
    #             'rm': ('__remove', {'targets[]': True}),
    #             'upload': ('__upload', {'target': True}),
    #            }

    # def get_init_params(self):
    #     """ Returns a dict which is used in response to a client init request.

    #         The returned dict will be merged with response during the __open
    #         command.
    #     """
    #     return {'api': '2.0',
    #             'uplMaxSize': '128M',
    #             'options': {'separator': '/',
    #                         'disabled': [],
    #                         'archivers': {'create': [],
    #                                       'extract': []},
    #                         'copyOverwrite': 1}
    #            }

    # def get_allowed_http_params(self):
    #     """ Returns a list of parameters allowed during GET/POST requests.
    #     """
    #     return ['cmd', 'target', 'targets[]', 'current', 'tree',
    #             'name', 'content', 'src', 'dst', 'cut', 'init',
    #             'type', 'width', 'height', 'upload[]']

    # def get_volume(self, hash):
    #     """ Returns the volume which contains the file/dir represented by the
    #         hash.
    #     """
    #     try:
    #         volume_id, target = hash.split('_')
    #     except ValueError:
    #         raise Exception('Invalid target hash: %s' % hash)

    #     return self.volumes[volume_id]

    # def check_command_variables(self, command_variables):
    #     """ Checks the GET variables to ensure they are valid for this command.
    #         _commands controls which commands must or must not be set.

    #         This means command functions do not need to check for the presence
    #         of GET vars manually - they can assume that required items exist.
    #     """
    #     for field in command_variables:
    #         if command_variables[field] == True and field not in self.data:
    #             return False
    #         elif command_variables[field] == False and field in self.data:
    #             return False
    #     return True

    # def run_command(self, func_name, command_variables):
    #     """ Attempts to run the given command.

    #         If the command does not execute, or there are any problems
    #         validating the given GET vars, an error message is set.

    #         func: the name of the function to run (e.g. __open)
    #         command_variables: a list of 'name':True/False tuples specifying
    #         which GET variables must be present or empty for this command.
    #     """
    #     if not self.check_command_variables(command_variables):
    #         self.response['error'] = 'Invalid arguments'
    #         return

    #     func = getattr(self, '_' + self.__class__.__name__ + func_name, None)
    #     if not callable(func):
    #         self.response['error'] = 'Command failed'
    #         return

    #     try:
    #         func()
    #     except Exception as e:
    #         self.response['error'] = '%s' % e
    #         logger.exception(e)

    # def run(self, request):
    #     """ Main entry point for running commands. Attemps to run a command
    #         function based on info in request.GET.

    #         The command function will complete in one of two ways. It can
    #         set response, which will be turned in to an HttpResponse and
    #         returned to the client.

    #         Or it can set return_view, a Django View function which will
    #         be rendered and returned to the client.
    #     """

    #     self.request = request

    #     # Is this a POST or a GET?
    #     if request.method == 'POST':
    #         data_source = request.POST
    #     elif request.method == 'GET':
    #         data_source = request.GET

    #     # Copy allowed parameters from the given request's GET to self.data
    #     for field in self.get_allowed_http_params():
    #         if field in data_source:
    #             if field == "targets[]":
    #                 self.data[field] = data_source.getlist(field)
    #             else:
    #                 self.data[field] = data_source[field]

    #     # If a valid command has been specified, try and run it. Otherwise set
    #     # the relevant error message.
    #     commands = self.get_commands()
    #     if 'cmd' in self.data:
    #         if self.data['cmd'] in commands:
    #             cmd = commands[self.data['cmd']]
    #             self.run_command(cmd[0], cmd[1])
    #         else:
    #             self.response['error'] = 'Unknown command'
    #     else:
    #         self.response['error'] = 'No command specified'

    #     self.httpResponse = self.response
    #     return self.httpStatusCode, self.httpHeader, self.httpResponse

    # def __parents(self):
    #     """ Handles the parent command.

    #         Sets response['tree'], which contains a list of dicts representing
    #         the ancestors/siblings of the target object.

    #         The tree is not a tree in the traditional hierarchial sense, but
    #         rather a flat list of dicts which have hash and parent_hash (phash)
    #         values so the client can draw the tree.
    #     """
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response['tree'] = volume.get_tree(target,
    #                                             ancestors=True,
    #                                             siblings=True)

    # def __tree(self):
    #     """ Handles the 'tree' command.

    #         Sets response['tree'] - a list of children of the specified
    #         target Directory.
    #     """
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response['tree'] = volume.get_tree(target)

    # def __file(self):
    #     """ Handles the 'file' command.

    #         Sets return_view, which will cause read_file_view to be rendered
    #         as the response. A custom read_file_view can be given when
    #         initialising the connector.
    #     """
    #     target = self.data['target']
    #     volume = self.get_volume(target)

    #     # A file was requested, so set return_view to the read_file view.
    #     #self.return_view = self.read_file_view(self.request, volume, target)
    #     self.return_view = volume.read_file_view(self.request, target)

    # def __open(self):
    #     """ Handles the 'open' command.

    #         Sets response['files'] and response['cwd'].

    #         If 'tree' is requested, 'files' contains information about all
    #         ancestors, siblings and children of the target. Otherwise, 'files'
    #         only contains info about the target's immediate children.

    #         'cwd' contains info about the currently selected directory.

    #         If 'target' is blank, information about the root dirs of all
    #         currently-opened volumes is returned. The root of the first
    #         volume is considered to be the current directory.
    #     """
    #     if 'tree' in self.data and self.data['tree'] == '1':
    #         inc_ancestors = True
    #         inc_siblings = True
    #     else:
    #         inc_ancestors = False
    #         inc_siblings = False

    #     target = self.data['target']
    #     if target == '':
    #         # No target was specified, which means the client is being opened
    #         # for the first time and requires information about all currently
    #         # opened volumes.

    #         # Assume the first volume's root is the currently open directory.
    #         volume = self.volumes.itervalues().next()
    #         self.response['cwd'] = volume.get_info('')

    #         # Add relevant tree information for each volume
    #         for volume_id in self.volumes:
    #             volume = self.volumes[volume_id]
    #             self.response['files'] = volume.get_tree('',
    #                                                      inc_ancestors,
    #                                                      inc_siblings)
    #     else:
    #         # A target was specified, so we only need to return info about
    #         # that directory.
    #         volume = self.get_volume(target)
    #         self.response['cwd'] = volume.get_info(target)
    #         self.response['files'] = volume.get_tree(target,
    #                                                  inc_ancestors,
    #                                                  inc_siblings)

    #     # If the request includes 'init', add some client initialisation
    #     # data to the response.
    #     if 'init' in self.data:
    #         self.response.update(self.get_init_params())

    # def __mkdir(self):
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response['added'] = [volume.mkdir(self.data['name'], target)]

    # def __mkfile(self):
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response['added'] = [volume.mkfile(self.data['name'], target)]

    # def __rename(self):
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response.update(volume.rename(self.data['name'], target))

    # def __list(self):
    #     target = self.data['target']
    #     volume = self.get_volume(target)
    #     self.response['list'] = volume.list(target)

    # def __paste(self):
    #     targets = self.data['targets[]']
    #     source = self.data['src']
    #     dest = self.data['dst']
    #     cut = (self.data['cut'] == '1')
    #     source_volume = self.get_volume(source)
    #     dest_volume = self.get_volume(dest)
    #     if source_volume != dest_volume:
    #         raise Exception('Moving between volumes is not supported.')
    #     self.response.update(dest_volume.paste(targets, source, dest, cut))

    # def __remove(self):
    #     targets = self.data['targets[]']
    #     self.response['removed'] = []
    #     # Because the targets might not all belong to the same volume, we need
    #     # to lookup the volume and call the remove() function for every target.
    #     for target in targets:
    #         volume = self.get_volume(target)
    #         self.response['removed'].append(volume.remove(target))

    # def __upload(self):
    #     parent = self.data['target']
    #     volume = self.get_volume(parent)
    #     self.response.update(volume.upload(self.request.FILES, parent))
