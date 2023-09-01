from django.core.exceptions import PermissionDenied


class IsTaskCreatorMixin:
    def check_task_permission(self, request, *args, **kwargs):
        task = self.get_object()

        if task.owner != request.user:
            raise PermissionDenied("You don't have permission to perform this action.")


class IsTaskCreatorUpdateMixin(IsTaskCreatorMixin):
    def get(self, request, *args, **kwargs):
        self.check_task_permission(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.check_task_permission(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.check_task_permission(request, *args, **kwargs)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.check_task_permission(request, *args, **kwargs)
        return super().patch(request, *args, **kwargs)


class IsTaskCreatorDeleteMixin(IsTaskCreatorMixin):
    def delete(self, request, *args, **kwargs):
        self.check_task_permission(request, *args, **kwargs)
        return super().delete(request, *args, **kwargs)
