# Reddit Network Analysis tool

## Team Members
Catarina Boto - https://www.linkedin.com/in/catarinaboto/

## Tool Description
This tool starts out from one node (either a redditor or a subreddit) and returns the redditors and subreddits that have interacted with this node. The number of iterations can be configured. It returns a .gexf file.

## Installation
**Note** This doesn't work yet, I didn't have time to set it up. 

This section includes detailed instructions for installing the tool, including any terminal commands that need to be executed and dependencies that need to be installed. Instructions should be understandable by non-technical users (e.g. someone who knows how to open a terminal and run commands, but isn't necessarily a programmer), for example:

1. Make sure you have Python version 3.8 or greater installed

2. Download the tool's repository using the command:

        git clone https://github.com/bellingcat/hackathon-submission-template.git

3. Move to the tool's directory and install the tool

        cd hackathon-submission-template
        pip install .

## Usage
This sections includes detailed instructions for using the tool. If the tool has a command-line interface, include common commands and arguments, and some examples of commands and a description of the expected output. If the tool has a graphical user interface or a browser interface, include screenshots and describe a common workflow.

Just run:
``
python3 main.py --root bellingcat --type 2
``
to try it out.
--root is the root node. Can be a subreddit or a redditor.
--type can be either 1 or 2, 1=redditor, 2=subreddit

## Additional Information
This section includes any additional information that you want to mention about the tool, including:
- Potential next steps for the tool (i.e. what you would implement if you had more time)
- Any limitations of the current implementation of the tool
- Motivation for design/architecture decisions# Reddit-Network-Analysis
