# the flow of the things

- i guess you have a folder with the data `data-folder`
- set up git repository on github
- clone created empty repo to your PC
`git clone https://github.com/ajankowski/tiny_scripts.git`

`git remote remove origin`

`git remote add origin https://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@github.com/ajankowski/tiny_scripts.git`


- add your files to the the `repo` folder: 
`cp -r ./data-folder/* repo`
- add all your files in `repo` folder to git:
`git add ./*`
- commit your files locally:
`git commit -m "your commit message"`
- push your commit to remote `repo`  
`git push origin main` or `https://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@github.com/ajankowski/tiny_scripts.git`
- Later - always start with:
`git pull origin master`

# token instructions

let's walk through how to set up a personal access token on GitHub, remove the original remote, and how to add a new one with your token.

1. Go to your GitHub account, click on your profile picture icon in the top right corner, scroll down and click on *Settings*.
2. On the left hand side of the screen, there is a menu bar. Scroll down near the bottom of the menu, and click on *Developer Settings*.
3. Once again, on the left side of the screen, there is a menu bar. Click on *Personal access tokens*, and then click on *Generate new token*.
4. When the menu to create a token comes up, set your expiration date, set you permissions, and generate your token.
5. Copy your token down and **KEEP IT HANDY -** you will not be able to see this again

Now, go back to your terminal.  First thing we need to do is remove the remote so we can add it back using the token.  In the terminal, run:

`git remote remove origin`.

Now, run

`git remote add origin https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git`

and replace the `<PLACEHOLDERS>` with their respective value.  

Then you should be free to run `git push origin main` with no problems.  

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

### using token:

`git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git`