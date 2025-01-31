pipeline {
    agent any
    stages {
        stage("Stage-1") {
            steps {
                dir("Testing_Jenkins"){
                    echo "Inside the repo"
                    sh "ls"
                }
            }
        }
        stage("Stage-2") {
            steps {
                dir("C:/Users/Administrator/Desktop/QE_COE/genai_venv/Scripts"){
                    echo "Inside stage-2"
                    sh "activate"
                    echo "completed stage-2"
                }
            }
        }
        stage("Stage-3") {
            steps {
                sh "python test1.py"
            }
        }
    }
}
