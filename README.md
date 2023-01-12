# Light-O-Rama-Automation

Preliminary exploration into automating conversion from audio files into Christmas / Halloween light shows. 

This is a very slow and cumbersome process to do manually, and I am hoping to find a way to generalize it. My Dad loves his Christmas lights, and I want to save him time and energy. 

My early efforts have been unsucessful so far due to the complexity of the problem. I initially believed that audio feature extraction would be sufficient detail to learn light show conversion, but there are patterns and dependencies between units that cannot be captured in a singular time unit. 

# TODO
* Use only Unit 1 as output (simplify)
* Create converter for compressed files (gain access to many more files) - https://github.com/Cryptkeeper/lightorama-protocol
  * Include Halloween songs as well to maximimize dataset (underlying principles should be the same)
* Conduct more rigorous correlation examination and exclude features that appear to have little correlation with sequence
  * In my brief initial examination, there seemed to be roughly half of the extracted features that had essentially zero correlation with any of the units
* Include some amount of previous sequence information in training input
  * I.e. n previous centiseconds output + n previous centiseconds audio + this centisecond audio
  * Domain knowledge would imply that the previous sequence choices are very important for current sequence choice
