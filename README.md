<h1>Summary</h1>
This project is an exercise for analyzing market price trends in the crypto market.
</br>
</br>
The example service calculates the moving average of the price of a given stock, using data from the last 5 seconds of realtime trading data.
</br>
</br>
Datasource:
https://finnhub.io/

<h1>Deployment</h1>

The repository is set up with docker in mind. This command should create every container and deploy the application.

`docker compose up`

<h1>Usage</h1>

If docker is running locally, you can check the result at
http://localhost:5050/

A sample response looks like this
</br>
</br>
`{"data":{"moving_average":[90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0,90488.0]}}`