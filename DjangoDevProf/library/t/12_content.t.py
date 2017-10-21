__author__ = 'freddy'
from TAP.Simple   import *

import library.Rules.Filters.libs.Content


plan(9)

string = "/* Single line comment*/ \\n CREATE TABLE test_user (name VARCHAR(25) NOT NULL, PRIMARY KEY(name));"
string_two_lines = """

INSERT INTO myapp_person (first_name, last_name) VALUES ('John', 'Lennon');
\n INSERT INTO myapp_person (first_name, last_name) VALUES ('Paul', 'McCartney');
"""

ok(library.Rules.Filters.libs.Content.match_content_regex(string, r'((.*) (table|TABLE) (.*))'))
ok(library.Rules.Filters.libs.Content.match_content_regex(string, r'((.*) PRIMARY KEY((.*))(.*))'))
ok(not library.Rules.Filters.libs.Content.match_content_regex(string, r'((.*) PRIMARY KEY ((.*))(.*))'))


ok(library.Rules.Filters.libs.Content.match_content_string(string, "TABLE"))
ok(library.Rules.Filters.libs.Content.match_content_string(string, "PRIMARY KEY"))
ok(not library.Rules.Filters.libs.Content.match_content_string(string, "SELECT"))

ok(library.Rules.Filters.libs.Content.match_content_string_kmp(string, "TABLE"))
ok(library.Rules.Filters.libs.Content.match_content_string_kmp(string, "PRIMARY KEY"))
ok(not library.Rules.Filters.libs.Content.match_content_string_kmp(string, "SELECT"))
