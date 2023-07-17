# Analysing a Semantics-Aware Bug Seeding Tool’s Efficacy: A qualitative study with the SemSeed tool

## Artifact materials

This artifact contains the files used in SemSeed's replication. As mentioned in the article, the necessary files for running SemSeed can be found [here](https://github.com/sola-st/SemSeed/).

The "Sample Files" folder has the input files which were each placed in SemSeed's "\benchmarks\data" folder, substituting the default file "sample.js".

The Selected Files folder contains the code fragments which were used in the survey. These fragments are from files generated by SemSeed, and each one has the associated Similarity from the JSON file.

The script "search_similarity.py" was used to divide the total output in four quartiles divided by similarity and choose one random file from each quartile, while "similarity_display.py" shows graphs of an output's similarity distribution.

A copy of the survey can be found [here](https://forms.gle/5kQ9sdkYJAqrH1536)

"[Final] Survey on Synthetic Bugs for JavaScript.xlsx" has the survey's data and all calculations displayed as tables throughout the article.

We also provide a directory with example files that, for any reason, SemSeed could not seed bugs in.


## Problems with replicating SemSeed

As mentioned in our article, trying to run SemSeed following its repository's tutorial presented problems.

According to the tutorial, in order to run it, one needs to download the required Python libraries, which are listed in the file "requirements.txt" in the repository. Many of the libraries could not be directly downloaded. Some of them were not available with pip anymore, or at least not in the version listed in the requirements file. We contacted SemSeed’s authors to report these errors. In response, they suggested that we attempt updating to the most recent versions of the packages. If this approach proved successful, they requested that we create a pull request to update the ’requirements.txt’ file. 

However, many of the libraries had to be installed manually by searching pip’s repositories one by one for their most recent versions. Some libraries could not be found at all and were ignored. The process consisted on trying to run SemSeed, getting an error for a missing library, then searching pip or apt for the library before trying to run SemSeed again.

We also could not execute the tutorial's first part. This part consists of extracting new bug-seeding patterns, the same step 1 mentioned in Section 2.3.1 (How SemSeed works). Trying to run the step's listed commands resulted in errors. We discussed contacting SemSeed's authors again about this issue, as it would give further data to use with SemSeed for our analysis. However, for this preliminary study, we decided to focus on using the original article's model to be able to make a direct comparison with their findings.


