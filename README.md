These options apply to single part article processing:
Option	Description
-S	Process only single part articles.
-g	This option ("g" for "greedy") will download and process each unread article even if the subject does not contain a filename which matches the single part extension filter.
These options apply to multi-part article processing:
Option	Description
-M	Process only multi-part articles.
-i	Interactive preselection of multi-part articles.
These options apply to both single part and multi-part article processing:
Option	Description
-A	Enables disk-based article assembly. This will download the articles to disk (instead of RAM) prior to decoding.
-b file	Batch file processing. file should contain a list of article subjects (from the .log files; see -s), one per line, to be downloaded. Mutually exclusive with -I and -X.
-C	Cleans up filenames. Without -C, ubh will perform certain mandatory character substitutions. This option performs further cleanup of the file names by replacing all non-alphanumeric characters in a filename with the EVILCHAR. Kills all non-alphanumeric leading characters. This will eliminate spaces in filnames, as well as all other undesireable (and possibly illegal) characters.
-d	Diagnostic mode. Downloads and writes all unread articles in raw form. This occurs prior to single and multi-part filtering. It's very useful to look at the raw articles to see why they are failing to be selected for downloading. Helpful for reverse-engineering new or bizarre encoding formats. You can also use this to perform your own post-processing directly on the raw articles. Articles are output using the article ID as the file name with the extension .dump.
-D	Dump mode. Downloads and writes all selected single and complete multi-part article to disk, instead of decoding. Very useful to look at the raw articles to see why they are failing to be unencoded. Helpful for reverse-engineering new or bizarre encoding formats. You can also use this to perform your own post-processing directly on the raw articles.
-c file	Use file as configuration file, instead of the default. On Win32 platforms, the default is ubhrc. On Unix platforms, the default is .ubhrc.
    -G group	By default ubh will process every subscribed group in the .newsrc. This option specifies the name of one group to be processed. Note that group must exist in the .newsrc and must be subscribed.
-a	Process all articles, but disregard the newsrc (ie, consider all articles even if they are marked as read in the newsrc, and do not catch up the group at the end of processing of the group).
-f num	Process the first num articles. Updates newsrc.
-l num	Process the last num articles. Updates newsrc.
-s	Log all subjects to subjects.log. Log multi-part subjects to multiparts.log. Doesn't download anything. Disregards newsrc. If FORCEDIR is in effect, the names of the file will be prepended with the group name.
-I regexp	Inclusion search filter (double quote on command line). regexp is any valid Perl regular expression.
-X regexp	Exclusion search filter (double quote on command line). regexp is any valid Perl regular expression.
    -L	Long filenames - uses the article subject as the filename. This makes life easier because many folks encode their files with terribly vague filenames.
-n	Updates the .newsrc every time an article is processed, instead of waiting until the entire group has been processed.
-O opt	Tells ubh what to do when it downloads a file and a file by that name already exists. no tells ubh to create a unique filename (by prepending the article number to the filename). yes tells ubh to overwrite the existing file with the new file. skip tells ubh to skip the incoming file and keep the existing file. In the case of multipart uuencoded binaries, ubh will download the first part to determine the file name; if a file with the same name already exists, ubh will skip the rest of the parts for that binary. The default is no.
-r	Logs rejected subjects to rejects.log in the group directory. Logs rejected single part and multi-part articles. Excellent for quality control to see if ubh is rejecting any binaries, and essential for diagnosing why articles are being rejected. Normally the rejected articles will contain SPAM or discussion, but occasionally ubh will reject an arcane format or mal-formed MIME-formatted message. Rejected multi-part articles logged with this option in are in their assembled stated, prefaced by the headers from the first article.
-u	Prints out a brief usage summary.
-w	Prints out warranty information.
-y	chmod 0666 on all output files.
-Z	Produces lots and lots of logs.
-z	Marks articles that don't pass inclusion/exclusion as read. This cleans up the .newsrc dramatically.
