![x](https://raw.github.com/astanway/picnic/master/picnic.jpeg)

## Let's have a picnic
The author found himself the subject of a number of speaking engagements. The author wanted to be hip and cool and so he used the hip and cool HTML5 presentation libary called reveal.js

## BUT THE AUTHOR WAS LAZY
As the author was making his slides, he did not bother to download actual images. He merely linked to them in the big, scary Internet.

## This was bad
The author knows that the Internet breaks and shit and he didn't want his slides to break with it.

## So instead of just !@#$ downloading each image, the author wrote this.
Call <code>pic.py -s index.html</code>, for example, and watch as it magically downloads every <code>\<img\></code> tag to the /images folder and links to the newly created assets in the original file. Whoosh.

## TODO:
* Add CSS support
* Add support for directories
* Write it in node and publish on the NPM
