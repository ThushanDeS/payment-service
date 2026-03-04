# test-payment.ps1 - Clean version
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "TESTING PAYMENT SERVICE (Student C)" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# Test 1: Health Check
Write-Host "`n1. Testing Health Endpoint..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:5003/health" -UseBasicParsing -ErrorAction Stop
    Write-Host "   ✅ Health: $($response.status)" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Payment Service not running" -ForegroundColor Red
    Write-Host "   Make sure Student C started their service on port 5003"
    exit
}

# Test 2: Get All Fares
Write-Host "`n2. Getting All Fares..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:5003/api/fares/" -UseBasicParsing
    Write-Host "   ✅ Got $($response.Count) fares" -ForegroundColor Green
    if ($response.Count -gt 0) {
        $fare = $response[0]
        Write-Host "   Sample: Flight $($fare.flight_id) - $($fare.fare_class) - $$($fare.total)"
    }
} catch {
    Write-Host "   ❌ Failed to get fares" -ForegroundColor Red
}

# Test 3: Calculate Fare
Write-Host "`n3. Calculating Fare for FL001 with 2 passengers..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:5003/api/fares/FL001?passengers=2" -UseBasicParsing
    Write-Host "   ✅ Fare calculated" -ForegroundColor Green
    Write-Host "   Total: $$($response.total) for $($response.totalPassengers) passengers"
} catch {
    Write-Host "   ❌ Failed to calculate fare" -ForegroundColor Red
}

# Test 4: Process Payment
Write-Host "`n4. Processing Test Payment..." -ForegroundColor Yellow
try {
    $body = @{
        booking_reference = "BKG" + (Get-Random -Maximum 999999)
        user_id = "USR001"
        amount = 299.99
        payment_method = "credit_card"
        card_number = "4111111111111111"
        card_expiry = "12/25"
        card_cvv = "123"
    } | ConvertTo-Json

    $response = Invoke-RestMethod -Uri "http://localhost:5003/api/payments/" -Method Post -Body $body -ContentType "application/json" -UseBasicParsing
    
    Write-Host "   ✅ Payment processed" -ForegroundColor Green
    Write-Host "   Status: $($response.status)"
    if ($response.paymentId) {
        Write-Host "   Payment ID: $($response.paymentId)"
    }
} catch {
    Write-Host "   ❌ Failed to process payment" -ForegroundColor Red
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $errorBody = $reader.ReadToEnd() | ConvertFrom-Json
        Write-Host "   Error: $($errorBody.message)"
    }
}

Write-Host "`n=====================================" -ForegroundColor Cyan
Write-Host "✅ Tests Complete" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Cyan