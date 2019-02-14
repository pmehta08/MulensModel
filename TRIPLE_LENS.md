## Triple lens

**First decide on frame used - e.g. check [ob07349](https://ui.adsabs.harvard.edu/#abs/2016AJ....152..125B/abstract) and make sure triple lens params can be predicted using binary lens params.**

Jen also suggests primary at origin and axis pointing to second object.

My main idea - center of mass as origin and first object on X axis.

# To do:

* MagnificationCurve.get\_triple\_lens\_magnification (include hooks to hexa, quad and PSPL)
* ModelParameters.\_\_repr\_\_ - finish
* ModelParameters.\_check\_valid\_combination\_1\_source - this needs some thinking
* ModelParameters - all the new parameters starting at s\_21
* Trajectory.get\_xy
* TripleLens.point\_source\_magnification
* TripleLens.hexadecapole\_magnification

