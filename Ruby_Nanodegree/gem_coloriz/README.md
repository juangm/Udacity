# Gem Colorizr
**Gem Version => 0.0.1**
## Summary
This gem extend the class String generating methods to color your strings with the following possibles colors:
- Red
- Green
- Yellow
- Blue
- Pink
- Light blue
- White
- Light grey
- Black

Two additional methods to get the full list of options available (**colors**) and to display a sample of colors (**sample_colors**)

## Usage
```ruby
	require 'colorizr'	
```
For generating colorful strings you just need to append the color to the string, like in the following list of examples:
```ruby
	puts "This is blue text".blue
	puts "This is green text".green
	...
```
To know the list of available methods (colors available) or to get a list of sample with the methods, just call the following methods:
```ruby
	String.colors 			# return array of all possible colors names
	String.sample_colors 	# display list of all possible colors
```

## Installation process
* gem install colorizr

## License
The MIT License (MIT)