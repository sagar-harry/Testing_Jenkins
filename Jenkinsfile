pipeline {
    agent any
    stages {
        stage(''){
            steps {
                deleteDir()
            }
        }
        stage('Stage-1: Clone repository') {
            steps {
                bat 'git clone https://github.com/sagar-harry/Testing_Jenkins'
            }
        }
        
        stage("Stage-2: Navigate into repo") {
            steps {
                dir("Testing_Jenkins"){
                    echo "Inside the repo"
                }
            }
        }
        
        stage("Stage-3: Activate environment") {
            steps {
                dir("C:/Users/Administrator/Desktop/QE_COE/genai_venv/Scripts"){
                    bat "activate"
                    bat "cd C:/Users/Administrator/Desktop/QE_COE/Jenkins/.jenkins/workspace/testing-1 && python test1.py"
                    echo "Completed stage-2"
                    bat "dir"
                }
            }
        }
    }
}
