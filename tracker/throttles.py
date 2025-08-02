from rest_framework.throttling import SimpleRateThrottle

class DeviceThrottle(SimpleRateThrottle):
    scope = 'device'

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return None

        device_id = request.data.get('device')
        if not device_id:
            return None
        return f'throttle_device_{device_id}'

    def allow_request(self, request, view):
        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])

        self.now = self.timer()  
        self.history = [timestamp for timestamp in self.history if self.now - timestamp < 5]

        if len(self.history) >= 1:
            return self.throttle_failure()

        self.history.append(self.now)
        self.cache.set(self.key, self.history, 5)  
        return self.throttle_success()
