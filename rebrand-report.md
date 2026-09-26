# Smoker-Agent rebrand - verification report

Job status: failure

## analyze
```
warning • The value of the local variable 'parsedJsonStr' isn't used. Try removing the variable or using it • lib/services/task_executor.dart:372:15 • unused_local_variable
   info • Unnecessary braces in a string interpolation. Try removing the braces • lib/services/task_executor.dart:405:57 • unnecessary_brace_in_string_interps
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:715:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:717:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:719:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:721:9 • curly_braces_in_flow_control_structures
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:27:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:45:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:58:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/telegram_service.dart:90:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/telegram_service.dart:143:7 • avoid_print
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:40:66 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:45:35 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:61:38 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:62:36 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:66:40 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:67:38 • deprecated_member_use
  error • Target of URI doesn't exist: 'package:integration_test/integration_test.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:11:8 • uri_does_not_exist
  error • Target of URI doesn't exist: 'package:agent_native/agent_native.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:13:8 • uri_does_not_exist
  error • Undefined name 'IntegrationTestWidgetsFlutterBinding'. Try correcting the name to one that is defined, or defining the name • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:16:3 • undefined_identifier
  error • Undefined class 'AgentNative'. Try changing the name to the name of an existing class, or creating a class with the name 'AgentNative' • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:19:11 • undefined_class
  error • The function 'AgentNative' isn't defined. Try importing the library that defines 'AgentNative', correcting the name to the name of an existing function, or defining a function named 'AgentNative' • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:19:32 • undefined_function
  error • Target of URI doesn't exist: 'package:agent_native/agent_native.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/lib/main.dart:5:8 • uri_does_not_exist
  error • The method 'AgentNative' isn't defined for the type '_MyAppState'. Try correcting the name to the name of an existing method, or defining a method named 'AgentNative' • local_plugins/agent_native/example/lib/main.dart:20:30 • undefined_method
  error • Target of URI doesn't exist: 'package:agent_native_example/main.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/test/widget_test.dart:11:8 • uri_does_not_exist
  error • The name 'MyApp' isn't a class. Try correcting the name to match an existing class • local_plugins/agent_native/example/test/widget_test.dart:16:35 • creation_with_non_type
  error • Target of URI doesn't exist: 'package:agent_native/agent_native_method_channel.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/test/agent_native_method_channel_test.dart:3:8 • uri_does_not_exist
  error • Undefined class 'MethodChannelAgentNative'. Try changing the name to the name of an existing class, or creating a class with the name 'MethodChannelAgentNative' • local_plugins/agent_native/test/agent_native_method_channel_test.dart:8:3 • undefined_class
  error • The function 'MethodChannelAgentNative' isn't defined. Try importing the library that defines 'MethodChannelAgentNative', correcting the name to the name of an existing function, or defining a function named 'MethodChannelAgentNative' • local_plugins/agent_native/test/agent_native_method_channel_test.dart:8:39 • undefined_function
  error • Target of URI doesn't exist: 'package:agent_native/agent_native.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/test/agent_native_test.dart:2:8 • uri_does_not_exist
  error • Target of URI doesn't exist: 'package:agent_native/agent_native_platform_interface.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/test/agent_native_test.dart:3:8 • uri_does_not_exist
  error • Target of URI doesn't exist: 'package:agent_native/agent_native_method_channel.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/test/agent_native_test.dart:4:8 • uri_does_not_exist
  error • Classes and mixins can only implement other classes and mixins. Try specifying a class or mixin, or remove the name from the list • local_plugins/agent_native/test/agent_native_test.dart:9:16 • implements_non_class
warning • The method doesn't override an inherited method. Try updating this class to match the superclass, or removing the override annotation • local_plugins/agent_native/test/agent_native_test.dart:12:19 • override_on_non_overriding_member
  error • Undefined class 'AgentNativePlatform'. Try changing the name to the name of an existing class, or creating a class with the name 'AgentNativePlatform' • local_plugins/agent_native/test/agent_native_test.dart:16:9 • undefined_class
  error • Undefined name 'AgentNativePlatform'. Try correcting the name to one that is defined, or defining the name • local_plugins/agent_native/test/agent_native_test.dart:16:47 • undefined_identifier
  error • Undefined name 'MethodChannelAgentNative'. Try correcting the name to one that is defined, or defining the name • local_plugins/agent_native/test/agent_native_test.dart:18:10 • undefined_identifier
  error • The name 'MethodChannelAgentNative' isn't a type, so it can't be used as a type argument. Try correcting the name to an existing type, or defining a type named 'MethodChannelAgentNative' • local_plugins/agent_native/test/agent_native_test.dart:19:42 • non_type_as_type_argument
  error • Undefined class 'AgentNative'. Try changing the name to the name of an existing class, or creating a class with the name 'AgentNative' • local_plugins/agent_native/test/agent_native_test.dart:23:5 • undefined_class
  error • The function 'AgentNative' isn't defined. Try importing the library that defines 'AgentNative', correcting the name to the name of an existing function, or defining a function named 'AgentNative' • local_plugins/agent_native/test/agent_native_test.dart:23:37 • undefined_function
  error • Undefined name 'AgentNativePlatform'. Try correcting the name to one that is defined, or defining the name • local_plugins/agent_native/test/agent_native_test.dart:25:5 • undefined_identifier
  error • Target of URI doesn't exist: 'package:flutter_overlay_window_example/home_page.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/flutter_overlay_window/example/lib/main.dart:2:8 • uri_does_not_exist
  error • Target of URI doesn't exist: 'package:flutter_overlay_window_example/overlays/true_caller_overlay.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/flutter_overlay_window/example/lib/main.dart:3:8 • uri_does_not_exist
  error • Invalid constant value • local_plugins/flutter_overlay_window/example/lib/main.dart:16:13 • invalid_constant
  error • The function 'TrueCallerOverlay' isn't defined. Try importing the library that defines 'TrueCallerOverlay', correcting the name to the name of an existing function, or defining a function named 'TrueCallerOverlay' • local_plugins/flutter_overlay_window/example/lib/main.dart:16:13 • undefined_function
  error • Invalid constant value • local_plugins/flutter_overlay_window/example/lib/main.dart:33:13 • invalid_constant
  error • The method 'HomePage' isn't defined for the type '_MyAppState'. Try correcting the name to the name of an existing method, or defining a method named 'HomePage' • local_plugins/flutter_overlay_window/example/lib/main.dart:33:13 • undefined_method
  error • Target of URI doesn't exist: 'package:flutter_overlay_window_example/main.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/flutter_overlay_window/example/test/widget_test.dart:11:8 • uri_does_not_exist
  error • The name 'MyApp' isn't a class. Try correcting the name to match an existing class • local_plugins/flutter_overlay_window/example/test/widget_test.dart:16:35 • creation_with_non_type
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:94:17 • no_leading_underscores_for_local_identifiers
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:114:17 • no_leading_underscores_for_local_identifiers
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:125:17 • no_leading_underscores_for_local_identifiers
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:142:17 • no_leading_underscores_for_local_identifiers
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:153:34 • no_leading_underscores_for_local_identifiers
   info • The local variable '_res' starts with an underscore. Try renaming the variable to not start with an underscore • local_plugins/flutter_overlay_window/lib/src/overlay_window.dart:161:17 • no_leading_underscores_for_local_identifiers
   info • Don't invoke 'print' in production code. Try using a logging framework • test_parse.dart:18:5 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • test_parse.dart:23:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • test_parse.dart:25:7 • avoid_print

147 issues found. (ran in 6.6s)
```

## test
```
(not run)
```

## build
```
(not run)
```

## analyze (all severities, first 120 lines)
```
Analyzing private-agent...                                      

   info • 'dialogBackgroundColor' is deprecated and shouldn't be used. Use DialogThemeData.backgroundColor instead. This feature was deprecated after v3.27.0-0.1.pre. Try replacing the use of the deprecated member with the replacement • lib/main.dart:21:9 • deprecated_member_use
   info • 'background' is deprecated and shouldn't be used. Use surface instead. This feature was deprecated after v3.18.0-0.1.pre. Try replacing the use of the deprecated member with the replacement • lib/main.dart:25:11 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/main.dart:160:50 • deprecated_member_use
warning • Unused import: 'dart:convert'. Try removing the import directive • lib/models/saved_skill.dart:1:8 • unused_import
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/overlay_main.dart:367:39 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/overlay_main.dart:399:35 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:577:48 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:580:50 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:762:43 • deprecated_member_use
   info • Unnecessary 'const' keyword. Try removing the keyword • lib/screens/home_screen.dart:786:25 • unnecessary_const
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:856:53 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:863:55 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:899:53 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:985:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:986:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:988:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:989:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1006:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1007:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1009:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1010:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1032:60 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1083:43 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1226:59 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1232:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1281:63 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1286:39 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1292:45 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1319:43 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/home_screen.dart:1324:41 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:476:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:477:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:479:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:480:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:497:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:498:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:500:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:501:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:533:54 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:542:42 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:602:57 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:613:43 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:619:59 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:681:41 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:737:58 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:746:53 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:916:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:994:30 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:995:57 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1000:33 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1018:61 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1221:47 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1224:49 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1280:51 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1346:57 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1354:41 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1365:53 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1414:58 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/onboarding_screen.dart:1419:33 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/settings_screen.dart:262:59 • deprecated_member_use
   info • Don't use 'BuildContext's across async gaps, guarded by an unrelated 'mounted' check. Guard a 'State.context' use with a 'mounted' check on the State, and other BuildContext use with a 'mounted' check on the BuildContext • lib/screens/settings_screen.dart:715:50 • use_build_context_synchronously
warning • The declaration '_buildShizukuCard' isn't referenced. Try removing the declaration of '_buildShizukuCard' • lib/screens/settings_screen.dart:937:10 • unused_element
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/task_history_screen.dart:139:66 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/task_history_screen.dart:183:78 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/task_history_screen.dart:185:97 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/task_history_screen.dart:222:92 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/screens/task_history_screen.dart:247:58 • deprecated_member_use
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/ai_service.dart:651:7 • avoid_print
   info • Use the null-aware marker '?' rather than a null check via an 'if'. Try using '?' • lib/services/alarm_service.dart:16:11 • use_null_aware_elements
   info • Use the null-aware marker '?' rather than a null check via an 'if'. Try using '?' • lib/services/alarm_service.dart:39:11 • use_null_aware_elements
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:54:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:82:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:103:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:121:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:136:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/chat_history_service.dart:148:7 • avoid_print
   info • Use the null-aware marker '?' rather than a null check via an 'if'. Try using '?' • lib/services/communication_service.dart:81:11 • use_null_aware_elements
   info • Use the null-aware marker '?' rather than a null check via an 'if'. Try using '?' • lib/services/communication_service.dart:82:11 • use_null_aware_elements
warning • The value of the local variable 'count' isn't used. Try removing the variable or using it • lib/services/screen_automation_service.dart:97:9 • unused_local_variable
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:199:31 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:200:34 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:201:34 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:202:37 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:203:36 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:204:65 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/screen_automation_service.dart:205:12 • curly_braces_in_flow_control_structures
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/skill_memory_service.dart:30:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/skill_memory_service.dart:40:7 • avoid_print
warning • Unnecessary cast. Try removing the cast • lib/services/task_executor.dart:305:28 • unnecessary_cast
warning • The value of the local variable 'parsedJsonStr' isn't used. Try removing the variable or using it • lib/services/task_executor.dart:372:15 • unused_local_variable
   info • Unnecessary braces in a string interpolation. Try removing the braces • lib/services/task_executor.dart:405:57 • unnecessary_brace_in_string_interps
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:715:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:717:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:719:9 • curly_braces_in_flow_control_structures
   info • Statements in an if should be enclosed in a block. Try wrapping the statement in a block • lib/services/task_executor.dart:721:9 • curly_braces_in_flow_control_structures
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:27:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:45:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/task_history_logger.dart:58:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/telegram_service.dart:90:7 • avoid_print
   info • Don't invoke 'print' in production code. Try using a logging framework • lib/services/telegram_service.dart:143:7 • avoid_print
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:40:66 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:45:35 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:61:38 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:62:36 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:66:40 • deprecated_member_use
   info • 'withOpacity' is deprecated and shouldn't be used. Use .withValues() to avoid precision loss. Try replacing the use of the deprecated member with the replacement • lib/widgets/message_bubble.dart:67:38 • deprecated_member_use
  error • Target of URI doesn't exist: 'package:integration_test/integration_test.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:11:8 • uri_does_not_exist
  error • Target of URI doesn't exist: 'package:agent_native/agent_native.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:13:8 • uri_does_not_exist
  error • Undefined name 'IntegrationTestWidgetsFlutterBinding'. Try correcting the name to one that is defined, or defining the name • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:16:3 • undefined_identifier
  error • Undefined class 'AgentNative'. Try changing the name to the name of an existing class, or creating a class with the name 'AgentNative' • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:19:11 • undefined_class
  error • The function 'AgentNative' isn't defined. Try importing the library that defines 'AgentNative', correcting the name to the name of an existing function, or defining a function named 'AgentNative' • local_plugins/agent_native/example/integration_test/plugin_integration_test.dart:19:32 • undefined_function
  error • Target of URI doesn't exist: 'package:agent_native/agent_native.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/lib/main.dart:5:8 • uri_does_not_exist
  error • The method 'AgentNative' isn't defined for the type '_MyAppState'. Try correcting the name to the name of an existing method, or defining a method named 'AgentNative' • local_plugins/agent_native/example/lib/main.dart:20:30 • undefined_method
  error • Target of URI doesn't exist: 'package:agent_native_example/main.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/example/test/widget_test.dart:11:8 • uri_does_not_exist
  error • The name 'MyApp' isn't a class. Try correcting the name to match an existing class • local_plugins/agent_native/example/test/widget_test.dart:16:35 • creation_with_non_type
  error • Target of URI doesn't exist: 'package:agent_native/agent_native_method_channel.dart'. Try creating the file referenced by the URI, or try using a URI for a file that does exist • local_plugins/agent_native/test/agent_native_method_channel_test.dart:3:8 • uri_does_not_exist
  error • Undefined class 'MethodChannelAgentNative'. Try changing the name to the name of an existing class, or creating a class with the name 'MethodChannelAgentNative' • local_plugins/agent_native/test/agent_native_method_channel_test.dart:8:3 • undefined_class
  error • The function 'MethodChannelAgentNative' isn't defined. Try importing the library that defines 'MethodChannelAgentNative', correcting the name to the name of an existing function, or defining a function named 'MethodChannelAgentNative' • local_plugins/agent_native/test/agent_native_method_channel_test.dart:8:39 • undefined_function
```
