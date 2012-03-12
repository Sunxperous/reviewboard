from reviewboard.scmtools.core import SCMClient, SCMTool, HEAD, PRE_CREATION
    supports_authentication = True
        super(GitTool, self).__init__(repository)

        local_site_name = None

        if repository.local_site:
            local_site_name = repository.local_site.name

        self.client = GitClient(repository.path, repository.raw_file_url,
                                repository.username, repository.password,
                                repository.encoding, local_site_name)
    def parse_diff_revision(self, file_str, revision_str, moved=False,
                            *args, **kwargs):
        elif revision != PRE_CREATION and not moved and revision != '':
            # Moved files with no changes has no revision,
            # so don't validate those.
    def check_repository(cls, path, username=None, password=None,
                         local_site_name=None):
        client = GitClient(path, local_site_name=local_site_name)
        super(GitTool, cls).check_repository(client.path, username, password,
                                             local_site_name)
        # Parse the extended header to save the new file, deleted file,
        # mode change, file move, and index.
        if self._is_new_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
        elif self._is_deleted_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
            linenum += 1
            file_info.deleted = True
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
        elif self._is_moved_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum + 2] + "\n"
            linenum += 3
            file_info.moved = True
            file_info.data += self.lines[linenum] + "\n"
    def _is_new_file(self, linenum):
        return self.lines[linenum].startswith("new file mode")
    def _is_deleted_file(self, linenum):
        return self.lines[linenum].startswith("deleted file mode")
    def _is_moved_file(self, linenum):
        return (self.lines[linenum].startswith("similarity index") and
                self.lines[linenum + 1].startswith("rename from") and
                self.lines[linenum + 2].startswith("rename to"))

class GitClient(SCMClient):
    def __init__(self, path, raw_file_url=None, username=None, password=None,
                 encoding='', local_site_name=None):
        super(GitClient, self).__init__(self._normalize_git_url(path),
                                        username=username,
                                        password=password)

        self.encoding = encoding
        self.local_site_name = local_site_name
            return self.get_file_http(self._build_raw_url(path, revision),
                                      path, revision)
                # We want to make sure we can access the file successfully,
                # without any HTTP errors. A successful access means the file
                # exists. The contents themselves are meaningless, so ignore
                # them. If we do successfully get the file without triggering
                # any sort of exception, then the file exists.
                self.get_file(path, revision)
                return True
            except Exception:
                return False
        return SCMTool.popen(['git'] + args,
                             local_site_name=self.local_site_name)
            return 'ssh://%s%s%s' % (m.group('username') or '',