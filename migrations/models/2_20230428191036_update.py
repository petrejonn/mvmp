from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "reset_password_expires" TIMESTAMPTZ;
        ALTER TABLE "user" RENAME COLUMN "disabled" TO "is_active";
        ALTER TABLE "user" ADD "activation_token" VARCHAR(100);
        ALTER TABLE "user" ADD "reset_password_token" VARCHAR(100);
        ALTER TABLE "user" ALTER COLUMN "username" TYPE VARCHAR(32) USING "username"::VARCHAR(32);
        ALTER TABLE "user" ALTER COLUMN "hashed_password" TYPE VARCHAR(100) USING "hashed_password"::VARCHAR(100);
        ALTER TABLE "user" ALTER COLUMN "email" TYPE VARCHAR(254) USING "email"::VARCHAR(254);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME COLUMN "is_active" TO "disabled";
        ALTER TABLE "user" DROP COLUMN "reset_password_expires";
        ALTER TABLE "user" DROP COLUMN "activation_token";
        ALTER TABLE "user" DROP COLUMN "reset_password_token";
        ALTER TABLE "user" ALTER COLUMN "username" TYPE VARCHAR(255) USING "username"::VARCHAR(255);
        ALTER TABLE "user" ALTER COLUMN "hashed_password" TYPE VARCHAR(255) USING "hashed_password"::VARCHAR(255);
        ALTER TABLE "user" ALTER COLUMN "email" TYPE VARCHAR(255) USING "email"::VARCHAR(255);"""
