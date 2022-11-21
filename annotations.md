[Annotations](https://github.com/cheesemid/cs482-project/blob/annotation/annotations.json)

DEXTR is a helpful tool for image annotation. It uses an ML model to detect edges and boundaries of an object based on extreme points that the user inputs. The model uses contrasts and color differences to accurately find all of the boundaries of an object.  

When I used DEXTR for annotations in CVAT, it was very helpful and powerful but I also noticed its shortcomings. Some of the images that I downloaded were low resolution and the blurryness in these images made it difficult for DEXTR to effectively detect the objects in it. Often times I had to use other tools that CVAT offered to correctly annotate the image.  

Another scenario where DEXTR had difficulty is when there is low contrast around edges. There were many images where white objects were on white backgrounds and DEXTR was unable to correctly detect the object. Other times, when annotating shiny or metal objects, the differences in contrast when light was shining on the object made it troublesome for DEXTR to function properly.  

Overall, DEXTR made the annotation process much quicker and easier but I still had to rely on other tools from CVAT to accurately annotate objects in situations where DEXTR was unable to.