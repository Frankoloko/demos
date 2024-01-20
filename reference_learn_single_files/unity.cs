// ###########################################################################################################
// MASTERING COMMUNICATION BETWEEN SCRIPTS/OBJECTS

// +-------------+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
// |             | You need a return | You have hundreds of object types | Explanation                                                                                                                                                  |
// +-------------+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
// | Inheritance |         Y         |                 N                 | It's a stable design but you can't have hundreds of objects inheriting, it's unmanageable (spaghetti code)                                                   |
// +-------------+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
// | SendMessage |         N         |                 Y                 | You have no care about the response. Bullet does "TakeDamage(5)". Doesn't matter if it hits a wall (does no damage) or a enemy (takes the damage).           |
// |             |                   |                                   | Also decouples/modularizes code greatly which is good (anti spaghetti code). It is resource intensive so never use it in Update or heavy loops.              |
// +-------------+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
// | Interface   |         Y         |                 Y                 | Last resort, you only need this if you have hundreds of objects and you need the return value of the call. It's basically a SendMessage with a return value. |
// +-------------+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+


// ###########################################################################################################
// MASTERING SENDMESSAGE

// Rules for using SendMessage
//      1. SendMessage cannot be used on an inactive GameObject: gameObject.SetActive(false);
//      2. SendMessage cannot be used on prefabs. Basically, the object needs to have been initialized in the
//          scene. You can check this with  gameObject.scene.IsValid()