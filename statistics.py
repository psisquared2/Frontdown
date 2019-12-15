from file_methods import sizeof_fmt

# Statistics dictionary; will be updated by various functions
class statistics_module:
    def __init__(self):
        self.reset()
    def reset(self):
        # scanning phase
        self.scanning_errors = 0        # covers folder and file errors, because they cannot always be distinguished
        self.bytes_in_source = 0
        self.bytes_in_compare = 0
        self.files_in_source = 0
        self.files_in_compare = 0
        self.folders_in_source = 0
        self.folders_in_compare = 0
        # backup phase
        self.backup_errors = 0
        self.bytes_copied = 0
        self.files_copied = 0
        self.bytes_hardlinked = 0
        self.files_hardlinked = 0
    def scanning_protocol(self):
        return "\tSource:\t\t\t%d folders, %d files, %s\n\tCompare:\t\t%d folders, %d files, %s\n\tScanning errors:\t%d" % (self.folders_in_source, self.files_in_source, sizeof_fmt(self.bytes_in_source), self.folders_in_compare, self.files_in_compare, sizeof_fmt(self.bytes_in_compare), self.scanning_errors)
    def backup_protocol(self):
        return "\tCopied:\t\t\t%d files, %s\n\tHardlinked:\t\t%d files, %s\n\tBackup Errors:\t\t%d" % (self.files_copied, sizeof_fmt(self.bytes_copied), self.files_hardlinked, sizeof_fmt(self.bytes_hardlinked), self.backup_errors)
        
# global variable to be changed by the other functions
statistics = statistics_module()