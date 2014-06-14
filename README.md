python-yaml-to-java
===================

Simple python script to convert a yaml config file to Java constant, designed to use with Android flavor build

## Example

From yaml
```
AppBuildConfig:
    DEBUG: true
    URL: http://google.com
    Component1:
        APP_ID: "abcdefg"
        ENABLE_FEATURE_A: true
        ENABLE_FEATURE_B: true
        ENABLE_FEATURE_C: false

```

to Java
```
/* AUTO GEN CODE, DONT MODIFY
 * last compile: 2014-06-14 12:27:54.824181
 */
package io.github.billynyh;
public class AppBuildConfig {
    public static final boolean DEBUG = true;
    public static final String URL = "http://google.com";
    public static class Component1 {
        public static final boolean ENABLE_FEATURE_C = false;
        public static final boolean ENABLE_FEATURE_B = true;
        public static final boolean ENABLE_FEATURE_A = true;
        public static final String APP_ID = "abcdefg";
    }
}

```
