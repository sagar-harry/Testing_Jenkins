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
                script {
                    def venv_path = "C:/Users/Administrator/Desktop/QE_COE/genai_venv/Scripts"
                    def workspace_path = "C:/Users/Administrator/Desktop/QE_COE/Jenkins/.jenkins/workspace/testing-1"

                    bat """
                        cd ${venv_path}
                        call activate
                        cd ${workspace_path}
                        python test1.py
                    """
                    echo "Completed Stage-3"
                }
            }
        }
    }
}
