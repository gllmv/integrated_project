# integrated_project
Aeronautics design project


To set up your team project using Git, GitHub, and Visual Studio Code (VS Code), I'll guide you through some key steps for organizing your workflow and ensuring efficient collaboration.

### 1. **Basics of Git**

Git is a version control system that helps manage changes to files (like your Python code) over time. The main concepts to understand:
- **Repository (Repo)**: A directory that contains your project files and a history of their changes.
- **Commit**: A snapshot of your project at a specific time. When you make changes and commit them, they get saved with a message explaining what was done.
- **Branch**: A separate workspace within a repo. For example, you might have a `main` branch that holds the stable code, and each member can work on their own feature branches.
- **Merge**: Combining branches, usually after review, back into the main branch.
- **Pull/Push**: Pull means getting the latest changes from GitHub into your local repository, and Push sends your changes to GitHub.

### 2. **How to Use Git**

#### Step-by-step workflow:
1. **Install Git**: Ensure Git is installed on your machine. You can check this by running `git --version` in your terminal.
   
2. **Clone the Repo**:
   Once your project is on GitHub, each team member needs to clone the repo to their local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

3. **Create a Branch**:
   Before starting a feature or task, create a new branch:
   ```bash
   git checkout -b feature-name
   ```

4. **Stage and Commit Changes**:
   After working on your code, you stage the files you want to save and commit them:
   ```bash
   git add .
   git commit -m "Description of what you did"
   ```

5. **Push Your Branch**:
   Push your branch to GitHub:
   ```bash
   git push origin feature-name
   ```

6. **Pull and Merge Changes**:
   Regularly pull changes from the `main` branch to stay updated:
   ```bash
   git pull origin main
   ```
   When your feature is ready, you can open a Pull Request (PR) on GitHub to request a merge into the main branch. This PR can be reviewed by other members.

7. **Merge the PR**:
   Once approved, the feature branch can be merged back into the main branch.

### 3. **Setting Up Visual Studio Code**

VS Code integrates well with Git and GitHub, making collaboration easier.

#### Install Extensions:
1. **GitHub Pull Requests and Issues**: This extension helps manage PRs directly within VS Code.
2. **Python**: For Python development support (if not already installed).
3. **Live Share**: This extension allows real-time collaboration in the same workspace, which can be helpful for remote debugging or code reviews.

#### Git Integration:
1. **Git panel**: VS Code has a Git panel on the left sidebar where you can commit, push, pull, and view your branches.
2. **Cloning a Repo in VS Code**:
   - Go to `Source Control` > `Clone Repository`.
   - Paste your repo URL from GitHub, and VS Code will open the project after cloning.

#### Branch Management:
- You can easily switch or create branches via the bottom-left of the screen where it shows the current branch.
  
#### Pull Requests in VS Code:
- Once your changes are pushed, go to the `GitHub Pull Requests` tab, and you can create, review, or merge pull requests from within VS Code.

### 4. **Good Practices for Collaboration**

1. **Clear Commit Messages**: Always write meaningful commit messages that describe the changes. This makes tracking easier.
   
2. **Pull Frequently**: Always pull the latest changes before starting work to avoid conflicts.

3. **Branching Strategy**:
   - **Main branch**: Keep this branch stable with the working code.
   - **Feature branches**: Each team member should work on their own branch for specific tasks or features. Merging into the `main` branch only happens after review.

4. **Code Reviews**: Encourage peer reviews via pull requests before merging any feature branch into `main`.

5. **Issues & Tasks**: Use GitHub’s issue tracker to assign tasks, track bugs, and document improvements. This helps coordinate work.

By following this setup, your team will have a structured and organized workflow, ensuring smooth collaboration.
