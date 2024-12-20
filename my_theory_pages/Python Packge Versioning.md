A package version should only have a lower limit, if we know any previous versions won't work.

A package version should onyl have an upper limit, if we have tests to update before opening the package ceiling. If you don't have tests to update, then you should not have an upper ceiling, because it gives you no value to have an upper ceiling. But having an upper ceiling causes a lot of admin work if you ever want to move the version of a package up. Now you would need to go into every package and open up the ceiling limit, even though there is no point for having one in the first place.

That said, you should probably lock the upper limit to the next Major version, since Major versions are bound to have large breaking changes.