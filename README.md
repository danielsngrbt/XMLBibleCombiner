# XMLBibleCombiner
An easy way to combine two different XML Bibles, e.g. for displaying two translations in Presenter by WorshipTools.

## Usage
1. This tool uses the ElementTree library which should have come with your copy of Python. If not, you can find it here: https://github.com/python/cpython/blob/main/Lib/xml/etree/ElementTree.py. 
2. Then just import your two bibles. ElementTree automatically parses them and treats them as trees. Here I combined a German and a Russian Bible: 
  ```
  german = ET.parse('german_S2000.xml')
  russian = ET.parse('russian.xml')
  ```
3. The code is self-explanatory. The tool iterates through the first Bible, book by book, chapter by chapter, verse by verse, and tries to match every verse with the corresponding from the other translation. If there is no correspoding verse in the second Bible (e.g. in the russian), the program stops and expects you to change the XML file (for example, the russian bible sometimes counts a verse already to the next chapter). Your two Bibles hopefully match better than the ones I had to combine :). I tried to add a lookup-table where you can add known anomalies between the bibles, but I had the feeling its faster to just fix them in runtime.

## Tips
If you need XML bibles, the Zefania XML Bible Markup Language (https://sourceforge.net/projects/zefania-sharp/) provides you with a lot of different translations and tools, e.g. to convert a bible into XML format. 
Feel free to contact me, add issues etc. Since the presentation software that we use in church (https://www.worshiptools.com/presenter) doesn't have the option to show two different translations, this might be helpful to someone out there.
