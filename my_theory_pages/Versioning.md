# Level 0: Overwriting the same file

Here we have no system of versioning. You just overwrite the same file over and over.

### Problem

If you make a mistake or a file goes corrupt then you have lost all your progress.

# Level 1: Version number files

Here you save files with *_v001, *_v002, *_v003. This now gives us the backups we need if never versions are corrupt or we make mistakes.

### Problem

In this design we assume the latest version is the correct version. This assumption in itself is a problem, because a mistake could be make in a new version, or some testing is being done in a new version, in which case the latest is not the correct version to use.

# Level 2: Approved files

We now mark certain versions as Approved. Therefore we notify exactly which versions have been tested and are correct for others to use.

Note that this still involves the Latest concept. We now follow a Latest-Approved concept. In other words, if multiple files are Approve, then the Latest-Approved one is the correct one.